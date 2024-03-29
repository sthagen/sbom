# SBOM

Tree shaking for the minimal viable software bill of materials (SBOM).

[![license](badges/license-spdx-mit.svg)](https://git.sr.ht/~sthagen/sbom/tree/default/item/LICENSE)
[![Country of Origin](badges/country-of-origin-name-switzerland-neutral.svg)](https://git.sr.ht/~sthagen/sbom/tree/default/item/COUNTRY-OF-ORIGIN)
[![Export Classification Control Number (ECCN)](badges/export-control-classification-number_eccn-ear99-neutral.svg)](https://git.sr.ht/~sthagen/sbom/tree/default/item/EXPORT-CONTROL-CLASSIFICATION-NUMBER)
[![Configuration](badges/configuration-sbom.svg)](third-party/index.html)

[![Version](badges/latest-release.svg)](https://pypi.python.org/pypi/sbom/)
[![Downloads](badges/downloads-per-month.svg)](https://pepy.tech/project/sbom)
[![Python](badges/python-versions.svg)](https://pypi.python.org/pypi/sbom/)
[![Maintenance Status](badges/commits-per-year.svg)](https://git.sr.ht/~sthagen/sbom/log)

## Bug Tracker

Any feature requests or bug reports shall go to the [todos of sbom](https://todo.sr.ht/~sthagen/sbom).

## Primary Source repository

The main source of `sbom` is on a mountain in central Switzerland.
We use distributed version control (git).
There is no central hub.
Every clone can become a new source for the benefit of all.
The preferred public clone of `sbom` is:

* [at sourcehut](https://git.sr.ht/~sthagen/sbom) - a collection of tools useful for software development.

## Contributions

Please do not submit "pull requests" (I found no way to disable that "feature" on GitHub).
If you like to share small changes under the repositories license please kindly do so by sending a patchset.
You can either send such a patchset per email using [git send-email](https://git-send-email.io) or 
if you are a sourcehut user by selecting "Prepare a patchset" on the summary page of your fork at [sourcehut](https://git.sr.ht/).

## Support

Please kindly submit issues at <https://todo.sr.ht/~sthagen/sbom> or write plain text email to <~sthagen/sbom@lists.sr.ht> to submit patches and request support. Thanks.

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
