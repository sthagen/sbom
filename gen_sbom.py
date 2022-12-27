import pathlib

__all__ = ['sbom_sha256']

ENCODING = 'utf-8'
TARGET = """\
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with\
 SHA256 checksum ([$hash_8$ ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256\
 "sha256:$hash_full$")).\
"""


def sbom_sha256():
    """Fill in the data."""
    with open(pathlib.Path('sbom.json.sha256'), 'rt', encoding=ENCODING) as handle:
        hash_full = handle.read().strip()
    hash_8 = hash_full[:8]
    print(TARGET.replace('$hash_8$', hash_8).replace('$hash_full$', hash_full))
