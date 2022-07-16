# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
import pytest  # type: ignore

import xmlschema
import cyclonedx.bom.validator as cdx

import spdx
from spdx.parsers.tagvalue import Parser
from spdx.parsers.loggers import StandardLogger
from spdx.parsers.tagvaluebuilders import Builder


def _spdx_tv_validation_proxy(tv_file_path):
    """YAGNI"""
    p = Parser(Builder(), StandardLogger())
    p.build()
    with open(tv_file_path) as f:
        data = f.read()
        document, error = p.parse(data)
        return False if error else True


EXAMPLES_PATH = pathlib.Path("examples")
CDX_MVP_JSON_1_2_PATH = pathlib.Path(EXAMPLES_PATH, "cyclonedx-v1.2_sbom-minimal-schema-match.json")
CDX_TYPICAL_JSON_1_2_PATH = pathlib.Path(EXAMPLES_PATH, "cyclonedx-v1.2_sbom.json")
EMPTY_JSON_OBJECT_PATH = pathlib.Path(EXAMPLES_PATH, "empty_object.json")

CDX_TYPICAL_XML_1_0_PATH = pathlib.Path(EXAMPLES_PATH, "cyclonedx-v1.0_sbom.xml")
# TODO(sthagen) add test for v1.2 validation - requires the Apache 2.0 licensed v1.2 XSDs ...
CDX_TYPICAL_XML_1_2_PATH = pathlib.Path(EXAMPLES_PATH, "cyclonedx-v1.2_sbom.xml")

# TODO(sthagen) implement independent SPDX v2.2 validation
SPDX_TYPICAL_TV_2_2_PATH = pathlib.Path(EXAMPLES_PATH, "spdx-v2.2_sbom_tag-value.txt")


def test_deps_nok_cyclone_dx_validation_of_json_empty_object(capsys):
    assert cdx.is_valid(EMPTY_JSON_OBJECT_PATH, True) is False
    out, _ = capsys.readouterr()
    assert "'bomFormat' is a required property" in out


def test_deps_ok_cyclone_dx_validation_of_mvp_json_1_2(capsys):
    assert cdx.is_valid(CDX_MVP_JSON_1_2_PATH, True) is True
    out, _ = capsys.readouterr()
    assert not out.strip()


def test_deps_ok_cyclone_dx_validation_of_typical_json_1_2(capsys):
    assert cdx.is_valid(CDX_TYPICAL_JSON_1_2_PATH, True) is True
    out, _ = capsys.readouterr()
    assert not out.strip()


def test_deps_nok_cyclone_dx_validation_of_typical_xml_1_0():
    """
    TODO(sthagen) - consider issuing a PR at cyclonedx-bom upstream project
      Proposal is to change from v0.4.3 behavior to better use str(path) when
      calling further upstream xmlschema.XMLSchema(schema_path).is_valid(path)
    """
    message = (
        r"wrong type <class 'pathlib.PosixPath'> for 'source' attribute:"
        r" an ElementTree object or an Element instance or a string containing"
        r" XML data or an URL or a file-like object is required."
    )
    with pytest.raises(xmlschema.exceptions.XMLSchemaTypeError, match=message):
        cdx.is_valid(CDX_TYPICAL_XML_1_0_PATH, False)


def test_deps_ok_cyclone_dx_validation_of_typical_xml_1_0_patched(capsys):
    """
    TODO(sthagen) - remove "belt and braces" when upstream project fixes delegation
    """
    assert cdx.is_valid(str(CDX_TYPICAL_XML_1_0_PATH), False) is True
    out, _ = capsys.readouterr()
    assert not out.strip()


def test_deps_ok_spdx_validation_of_typical_tv_2_2(capsys):
    assert _spdx_tv_validation_proxy(SPDX_TYPICAL_TV_2_2_PATH) is False  # Cf. SPDX TODO above
    gibberish = (
        "true\n"
        "Package copyright text must be free form text, line: 21\n"
        "Found unknown tag : Relationship at line: 23\n"
        "FileChecksum must be a single line of text starting with 'SHA1:', line:29\n"
        "FileChecksum must be a single line of text starting with 'SHA1:', line:30\n"
        "FileCopyrightText must be one of NOASSERTION, NONE or free form text, line: 33"
    )
    out, _ = capsys.readouterr()
    assert out.strip() == gibberish
