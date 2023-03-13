# sbom

Tree shaking for the minimal viable software bill of materials (SBOM).

[License: MIT](https://github.com/sthagen/sbom/blob/default/LICENSE)

Third party dependencies are documented in the folder [third-party](docs/third-party/README.md).

[![version](https://img.shields.io/pypi/v/sbom.svg?style=flat)](https://pypi.python.org/pypi/sbom/)
[![downloads](https://pepy.tech/badge/sbom/month)](https://pepy.tech/project/sbom)
[![wheel](https://img.shields.io/pypi/wheel/sbom.svg?style=flat)](https://pypi.python.org/pypi/sbom/)
[![supported-versions](https://img.shields.io/pypi/pyversions/sbom.svg?style=flat)](https://pypi.python.org/pypi/sbom/)
[![supported-implementations](https://img.shields.io/pypi/implementation/sbom.svg?style=flat)](https://pypi.python.org/pypi/sbom/)

## Documentation

User and developer [documentation of sbom](https://codes.dilettant.life/docs/sbom).

## Bug Tracker

Any feature requests or bug reports shall go to the [todos of sbom](https://todo.sr.ht/~sthagen/sbom).

## Primary Source repository

The main source of `sbom` is on a mountain in central Switzerland.
We use distributed version control (git).
There is no central hub.
Every clone can become a new source for the benefit of all.
The preferred public clones of `sbom` are:

* [on codeberg](https://codeberg.org/sthagen/sbom) - a democratic community-driven, non-profit software development platform operated by Codeberg e.V.
* [at sourcehut](https://git.sr.ht/~sthagen/sbom) - a collection of tools useful for software development.

## Contributions

Please do not submit "pull requests" (I found no way to disable that "feature" on GitHub).
If you like to share small changes under the repositories license please kindly do so by sending a patchset.
You can either send such a patchset per email using [git send-email](https://git-send-email.io) or 
if you are a sourcehut user by pointing your browser to "[Prepare a patchset](https://git.sr.ht/~sthagen/sbom/send-email)".

## Status

Experimental.

## Terminology

* **baseline** - mandatory elements
* **consume** - an SBOM
* **crypto** - hashing, signing, and signature validation
* **extension** - sets of elements mandatory in addition to baseline
* **fuzz** - generate surrogate and poisoned SBOMs
* **merge** - an SBOM with other SBOMs or additional information
* **mock** - provide optimal testability
* **policy** - to apply
* **produce** - an SBOM
* **report** - anything from produce, transform, and consume
* **rule** - executing policies
* **transform** - one SBOM into another SBOM

## Safety, Security, and Data Protection Considerations

The current implementation **SHALL** only digest trustworthy data.  

Schema validation of JSON and XML formats requires specific measures to  
minimize vulnerabilities.

For example: The python xml parser implementation (etree) in  
use is presumably vulnerable against some attacks like *billion laughs*
and *quadratic blowup*.

Plans are to move towards a safer implementation like `defusedxml`
or any other hardened implementation.

The situation is similar for the JSON formats.

In summary and repeating the obvious:
> The current implementation **SHALL** only digest trustworthy data.

**Note**: The default branch is `default`.
