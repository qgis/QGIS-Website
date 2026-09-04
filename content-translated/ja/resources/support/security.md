---
Reviewed: 5 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: セキュリティ
type: page

---
{{<content-start >}}
# セキュリティ
## セキュリティ情報
QGISコミュニティはセキュリティを重視しています。QGISが重要な環境にも導入されていることを認識しています。このページでは、QGISプロジェクトが脆弱性およびセキュリティ問題にどのように対応するかについて説明します。
### What is a vulnerability in QGIS?
QGIS is a project that can be used in many contexts and has a rich set of features. To provide this functionality, it relies on many components, relying on a large base of external dependencies (e.g. GDAL, PROJ, Python libraries, Qt, etc.). Security issues in QGIS can arise in various scenarios, including, but not limited to, vulnerabilities in its dependencies, issues within QGIS code itself, or through the misuse of its Python bindings. Here are the main categories:
#### Vulnerabilies of underlying libraries
If you run a code scanner, most of the vulnerabilities listed are not related to QGIS, but to its dependencies. The specific version of the dependencies shipped with QGIS depends on the OS and packaging system being used.

**On Windows**, QGIS.org uses the OSGeo4W project to distribute a complete environment. The OSGeo4W build is fully maintained by the QGIS project.

OSGeo4W provides update scripts, allowing you to upgrade only the necessary libraries without the need to redownload the entire package. For more information on setting up these scripts for your deployment, refer to the [OSGeo4W documentation](https://trac.osgeo.org/osgeo4w/).

On **[Ubuntu / Debian](/resources/installation-guide/#debian--ubuntu)**, we provide QGIS binaries and work closely with packagers of OSGEO libraries (GDAL / PROJ / GRASS). For Python and Qt libraries, which rely on your operating system, please ensure they are updated regularly using your system's update manager. For Ubuntu/Debian, this typically involves using commands like `sudo apt update` and `sudo apt upgrade`.

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
If you believe you have found a security issue, such as vulnerabilities in QGIS or its dependencies, please do the following:
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
We can provide CVE identifiers, if you disclose your vulnerability via [Github advisories](https://github.com/qgis/QGIS/security) We won't affect CVE if the vulnerability concerns an upstream dependency.
### Security vulnerability management and vulnerability disclosure processes
Disclosures are discussed in private [Github advisories](https://github.com/qgis/QGIS/security)

Fixes are shipped as soon as possible in point releases - depending on the criticality of the issue.

If you want to secure your QGIS enterprise deployment, please ensure you are able to quickly deploy fixes to the machines you manage.

OSGeo4W provides update scripts that can run unattended. These scripts also allow you to upgrade only the necessary libraries without the need to re-download the entire package. For more information on setting up these scripts for your deployment, refer to the [OSGeo4W documentation](https://trac.osgeo.org/osgeo4w/).
### Are there independent security audit available ?
The latest public audit available has been conducted by the Swiss National Cyber Security Centre (NCSC) during a [pilot project for testing security vulnerabilities in open source software](https://www.bacs.admin.ch/en/25-ntc-oss-en).

{{<rich-list listLink="../media/ntc-test-report-qgis-v1-2025-10-13.pdf" linkAttr="download" layoutClass="third" listTitle="Security Audit QGIS Server and QWC2 - Test Report 2025.10.13 NCSC" listSubtitle="Download PDF" >}}

QGIS has been assessed privately by many organisations, sometimes in very sensitive context from security management to network utilities.<br />QGIS server, as it is a web server interacting with databases, is the most critical part. It has been hardened against SQL injections.
### Have penetration tests been conducted ?
QGIS Desktop is a desktop tool, not a SaaS software. It does not need a remote infrastructure.

QGIS server has been tested against vulnerabilities and follows a classical discoslure / fix procedure.
### Secure software development and code-review practices
A global overview of our security can be found using the [OpenSSF Scorecard report tool](https://securityscorecards.dev/viewer/?uri=github.com/qgis/QGIS).

Multi Factor authentication is mandatory on our Github repositories.
### Software release integrity and verification mechanisms
Every [available package](https://www.qgis.org/resources/installation-guide/) is available with a checksum. MacOS packages are notarized. We are aware of the risks of XZ style supply chain attack. The contributors can gain privileges only after a long and committed period, and after real world meeting during our contributor meetings.
### What is the supported versions and security patch/EOL policy
See <https://www.qgis.org/resources/roadmap/>.
### How is done the security management of third-party dependencies ?
QGIS.org endorses only Ubuntu/Debian and Windows packaging.

Dependency for Ubuntu/Debian relies on the user's distribution and is not of QGIS.org responsability.

Windows installer packages library, via the [OSGEO4W project](https://trac.osgeo.org/osgeo4w). Our maintainers are committed to react as fast as possible, depending on the vulnerability's criticity.
### Security controls or review processes applicable to third-party QGIS plugins
QGIS Desktop is packaged with a python plugin's installer, that allows users to install third party extensions, just like web browsers do.

See <https://plugins.qgis.org/docs/security-scanning>

As python execution in a desktop environment is inheriting all the privileges of a user, deployment in sensitive environments should deactivate direct access to this repository and replace it with an internal repository, allowing only audited plugins.
### Do you provide ISO 27001 certification, SOC 2, CRA attestation ?
No we don't. If you need them, please contact us and consider funding QGIS.org to absorb the work load those compliance requirements put on our shoulders. QGIS.org is not a service provider, and QGIS is avalaible following the term of the GPL 2 licence.
### Can QGIS.org fill my own compliance form ?
QGIS.org is a foundation run by donations and membership fees. We have limited resources among our volunteer and paid staff. We are currently seeing a tendency for each organisation to create its own form. We can't fill them out for you, but we will put as much information as possible here on the website to help you fill in those forms. As soon as those forms follow a national or international standard, we would be more than happy to publish them online.

For instance, you can find the US HECVAT and VPAT forms managed by the US user group, published at <https://www.qgis-us.org/hecvat/> and <https://www.qgis-us.org/vpat/>.

{{<content-end >}}
