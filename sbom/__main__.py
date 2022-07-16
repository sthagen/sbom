# -*- coding: utf-8 -*-
"""Visit folder tree with CycloneDX, SPDX, or SWID documents, validate these documents against baseline as well as extensions, and generate reports."""
import sys

import sbom.sbom as lint


def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    lint.main(argv)
