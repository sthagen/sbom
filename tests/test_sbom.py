# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
import pytest  # type: ignore

import cyclonedx.bom.validator as cdx

EMPTY_JSON_OBJECT_PATH = pathlib.Path("examples", "empty_object.json")


def test_deps_nok_cyclone_dx_validation_of_json_empty_object(capsys):
    assert cdx.is_valid(EMPTY_JSON_OBJECT_PATH, True) is False
    out, _ = capsys.readouterr()
    assert "'bomFormat' is a required property" in out
