
---
type: "page"
title: "Security"
subtitle: ""
draft: false
sidebar: true
Reviewed: 5 June 2024
Reviewer: Tim Sutton
---

{{< content-start >}}

## Security information

The QGIS community takes security seriously. We are aware that QGIS is deployed in sensitive environments. This page outlines how the QGIS project responds to vulnerabilities and security matters. 


### What is a vulnerability in QGIS?

QGIS is a project that can be used in many contexts and has a rich set of features. To provide this functionality, it relies on many components, relying on a large base of external dependencies (e.g. GDAL, PROJ, Python libraries, Qt, etc.). 
Security issues in QGIS can arise in various scenarios, including, but not limited to, vulnerabilities in its dependencies, issues within QGIS code itself, or through the misuse of its Python bindings. Here are the main categories:

#### Vulnerabilies of underlying libraries 

If you run a code scanner, most of the vulnerabilities listed are not related to QGIS, but to its dependencies. The specific version of the dependencies shipped with QGIS depends on the OS and packaging system being used. 

**On Windows**, QGIS.org uses the OSGeo4W project to distribute a complete environment. The OSGeo4W build is fully maintained by the QGIS project.

OSGeo4W provides update scripts, allowing you to upgrade only the necessary libraries without the need to redownload the entire package. For more information on setting up these scripts for your deployment, refer to the [OSGeo4W documentation](https://trac.osgeo.org/osgeo4w/).


On **[Ubuntu / Debian](/resources/installation-guide/#debian--ubuntu)**, we provide QGIS binaries and work closely with packagers of OSGEO libraries (GDAL / PROJ / GRASS).
For Python and Qt libraries, which rely on your operating system, please ensure they are updated regularly using your system's update manager. For Ubuntu/Debian, this typically involves using commands like `sudo apt update` and `sudo apt upgrade`.

Other Linux distribution packages are maintained by the community, such as Conda, FlatPak, etc. Any issue should be raised to the downstream maintainers.  

#### False positives

Receiving red flags from code scanner alerts can be alarming, but many of the current alerts are false positives, so keep calm and don't panic.

For example, a common false positive might involve the PostgreSQL client library (libpq) being flagged for server-side vulnerabilities, which do not apply to QGIS's use case.

When discovering a potential vulnerability, read the CVE report, go to the upstream project CVE description and please verify this really concerns QGIS. 

Please also communicate these findings to your code scanner vendor for catalog updates, to reduce the number of false positives being emitted in the future.

There is not a lot QGIS contributors can do to resolve reports where the classification of dependencies is not accurate in the CVE database.

### Vulnerabilities of QGIS itself

Those are extremely rare but can occur (as they can in any software).

QGIS server and QGIS Desktop have been written to limit the possibility of SQL injections and various known security vectors, and has been used by big corporations and governments for many years. 

## What to do if you think you have found a security issue

If you believe you have found a security issue, such as vulnerabilities in QGIS or its dependencies, please refer to the [security page]({{< ref "resources/support/security" >}}) for detailed information on how to report it responsibly. Before this, please do the following:

 - Check you are using the latest version of QGIS, and have a glance at the nightly version for potential ongoing changes (fixes or regressions).
 - Check if your issue concerns QGIS desktop or QGIS server.
 - Please check our [bug tracker](https://github.com/qgis/QGIS/issues) to see if we already have an existing and potential fix.
 - Assuming you still need to raise the issue, raise a private disclosure to the security teams via [our GitHub security page](https://github.com/qgis/QGIS/security). Please avoid publicly disclosing the vulnerability until it has been resolved to prevent potential exploitation.

#### Running python QGIS 

Python bindings allow you to extend QGIS by writing plugins, geoprocessing models, actions, project macros, or even rewrite a full application. 

In a desktop environment, any scripting language typically has full access to the user's resources and can execute arbitrary code with the permissions of the user. If you execute external code it can potentially do a lot of harm. 

The [QGIS plugins repository](https://plugins.qgis.org) is open for anyone to use to publish their work. We review submissions manually. We do not undertake advanced QA assessments of plugin code. Plugins should not bundle compiled code, so you know what you get in each plugin and are free to audit the code. 


If your are working in a sensitive environment, we advise you to :

- Carefully audit each plugin in a sandboxed environment before you allow your users to use it.
- Deploy your own plugin repository so that you can control which plugins are available to your users.
- Make use of the advanced customization capabilities of QGIS to constrain settings around connections, authentication etc.
- Don't only focus on code breaches, but also on user behavior regarding credentials and the risk of leaks in project files if users insist on using basic authentication (which will result in credentials being stored in plain text in project files).  
 

### Do we generate Common Vulnerabilities and Exposures (CVE)?  

Currently, QGIS project is **not** a CVE Numbering Authority (CNA), so we don't emit CVE identifiers. 


### Security Process and workflow

Disclosures are discussed in a private dedicated repository.

Fixes are shipped as soon as possible in point releases - depending on the criticality of the issue. 

If you want to secure your QGIS enterprise deployment, please ensure you are  able to quickly deploy fixes to the machines you manage. 

OSGeo4W provides update scripts that can run unattended. These scripts also  allow you to upgrade only the necessary libraries without the need to re-download the entire package. For more information on setting up these scripts for your deployment, refer to the [OSGeo4W documentation](https://trac.osgeo.org/osgeo4w/).



{{< content-end >}}
