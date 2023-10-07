# -*- coding: utf-8 -*-
import pathlib

import cyclonedx_py.parser.environment as cdx
from spdx_tools.spdx.parser.parse_anything import parse_file as parse_spdx_file

from sbom.sbom import parse


def test_parse():
    assert parse() is NotImplemented


def _spdx_tv_validation_proxy(tv_file_path):
    """YAGNI"""
    try:
        _ = parse_spdx_file(tv_file_path)
        return True
    except:
        return False


EXAMPLES_PATH = pathlib.Path('examples')
CDX_MVP_JSON_1_2_PATH = pathlib.Path(EXAMPLES_PATH, 'cyclonedx-v1.2_sbom-minimal-schema-match.json')
CDX_TYPICAL_JSON_1_2_PATH = pathlib.Path(EXAMPLES_PATH, 'cyclonedx-v1.2_sbom.json')
EMPTY_JSON_OBJECT_PATH = pathlib.Path(EXAMPLES_PATH, 'empty_object.json')

CDX_TYPICAL_XML_1_0_PATH = pathlib.Path(EXAMPLES_PATH, 'cyclonedx-v1.0_sbom.xml')
# TODO(sthagen) add test for v1.2 validation - requires the Apache 2.0 licensed v1.2 XSDs ...
CDX_TYPICAL_XML_1_2_PATH = pathlib.Path(EXAMPLES_PATH, 'cyclonedx-v1.2_sbom.xml')

# TODO(sthagen) implement independent SPDX v2.2 validation
SPDX_TYPICAL_TV_2_2_PATH = pathlib.Path(EXAMPLES_PATH, 'spdx-v2.2_sbom_tag-value.txt')


def test_deps_nok_cyclone_dx_validation_of_json_empty_object(capsys):
    _ = ''
    comp = cdx.Component.for_file(str(EMPTY_JSON_OBJECT_PATH), _)
    assert not comp.has_vulnerabilities()
    out, _ = capsys.readouterr()
    assert not out


def test_deps_ok_cyclone_dx_validation_of_mvp_json_1_2(capsys):
    _ = ''
    comp = cdx.Component.for_file(str(CDX_MVP_JSON_1_2_PATH), _)
    assert not comp.has_vulnerabilities()
    out, _ = capsys.readouterr()
    assert not out.strip()


def test_deps_ok_cyclone_dx_validation_of_typical_json_1_2(capsys):
    _ = ''
    comp = cdx.Component.for_file(str(CDX_TYPICAL_JSON_1_2_PATH), _)
    assert not comp.has_vulnerabilities()
    out, _ = capsys.readouterr()
    assert not out.strip()


def test_deps_nok_cyclone_dx_validation_of_typical_xml_1_0():
    """
    TODO(sthagen) - consider issuing a PR at cyclonedx-bom upstream project
      Proposal is to change from v0.4.3 behavior to better use str(path) when
      calling further upstream xmlschema.XMLSchema(schema_path).is_valid(path)
    """
    _ = ''
    assert cdx.Component.for_file(str(CDX_TYPICAL_XML_1_0_PATH), _)


def test_deps_ok_cyclone_dx_validation_of_typical_xml_1_0_patched(capsys):
    """
    TODO(sthagen) - remove "belt and braces" when upstream project fixes delegation
    """
    _ = ''
    comp = cdx.Component.for_file(str(CDX_TYPICAL_XML_1_0_PATH), _)
    assert not comp.has_vulnerabilities()
    out, _ = capsys.readouterr()
    assert not out.strip()


def test_deps_ok_spdx_validation_of_typical_tv_2_2(capsys):
    assert _spdx_tv_validation_proxy(SPDX_TYPICAL_TV_2_2_PATH) is False  # Cf. SPDX TODO above
    out, _ = capsys.readouterr()
    assert out.strip() == ''
