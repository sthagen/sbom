# -*- coding: utf-8 -*-
"""Generic linter for software Bill of Materials (SBOM) formats.

1. visit folder tree with CycloneDX, SPDX, or SWID documents
2. validate these documents against baseline as well as extensions, and
3. generate reports.
"""
import sys

import sbom.sbom as lint


def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    lint.main(argv)
