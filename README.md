# refactored-computing-machine
Tree shaking for the minimal viable SBOM.

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
