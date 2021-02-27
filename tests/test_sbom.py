# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
import pytest  # type: ignore

import cyclonedx.bom.validator as cdx

CDX_MVP_JSON_1_2_PATH = pathlib.Path("examples", "cyclonedx-v1.2_sbom-minimal-schema-match.json")
EMPTY_JSON_OBJECT_PATH = pathlib.Path("examples", "empty_object.json")


def test_deps_nok_cyclone_dx_validation_of_json_empty_object(capsys):
    assert cdx.is_valid(EMPTY_JSON_OBJECT_PATH, True) is False
    out, _ = capsys.readouterr()
    assert "'bomFormat' is a required property" in out


def test_deps_ok_cyclone_dx_validation_of_mvp_json_1_2(capsys):
    assert cdx.is_valid(CDX_MVP_JSON_1_2_PATH, True) is True
    out, _ = capsys.readouterr()
    assert not out.strip()
