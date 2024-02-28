
---
type: "page"
title: "Security"
subtitle: ""
draft: false
sidebar: true
---

{{< content-start  >}}



 

## Security information

The QGIS community takes security as a serious matter. We are aware that QGIS is deployed in sensitive environnements. 

For these reasons, this is how QGIS project acts to respond to vulnerabilities and security matters. 


Our main landing page for security issues is on our [Github's repositoy](https://github.com/qgis/QGIS/security).


### What is a vulnerability in QGIS ? 

QGIS is a broad project with several different components, relying on a large base of external dependencies (GDAL, Proj, python libraries, Qt, etc..). 

#### Vulnerabilies of underlying libraries 

If you run a code scanner, most of the vulnerabilities are not concerning QGIS, but its dependencies. 
The version of the dependencies shipped with your QGIS depends on the OS and packaging system you use. 

**On Windows**, we use OSGEO4W project to distribute a complete environnement, and we fully maintain it.

This installer is updated every month with various fixes and upgrades. If the latest version doesn't include a version fixing the vulnerability, please raise an issue on the dedicated [OSGEO4W bug tracker](https://trac.osgeo.org/osgeo4w/).

On Ubuntu / Debian, we provide QGIS binaries and work closely with packagers of OSGEO libraries (GDAL / Proj / GRASS).
But python and Qt libraries rely on your OS and you have to use your update manager here. 

#### False positives

We collect a lot of library upgrade due to false positive. For instance, PostgreSQL client library embedded in QGIS trigger vulnerabilities of the **server part**, which is not shipped with QGIS installer.  

Before blindly pushing your code scanner alerts, keep calm and don't panic. Read the CVE report, go to the upstream project CVE description and please verify this really concerns. 
Please also raise this to your code scanner vendor so that they update their catalog accordingly. We can't do anything from our side, but are flooded by those reports. This way you preserve the available bandwith of the contributors for the real issues. 

#### Vulnerabilities of QGIS itself

Those are extremely rare but can occur as in any software. 

If you found an issue: 
 - check you are using the latest version of QGIS, and have a glance at the nighlty version for potential ongoing changes
 - please check our [Bug tracker](https://github.com/qgis/QGIS/issues) for an already existing and potential fix
 - then only, raise a private disclosure to the security teams [our GitHub security page](https://github.com/qgis/QGIS/security).

QGIS server is a more critical part than QGIS desktop, since it is exposed to the web on public servers. It has been assessed against SQL injections and various known leaks by big corporations since years now. 
Please be specific in your disclosure if QGIS server is concerned or not. 



#### Running python QGIS 

QGIS offers python bindings so that you can extend it by writting plugins, geoprocessing models, actions, project macros, or even rewrite a full application based on pyQGIS. 

In a desktop environnement, any scripting language has full access to the userland ressources. If you execute blindly external code, it can do a lot of harm. 

QGIS main plugins repository is permissively open, but approval of plugins is still reviewed manually. We do not take advance QA assessment of plugin code. However we forbid to ship compiled code, so you know what you get and are free to audit the code. 


If your are working in a sensitive environnement, we advise you to :

- Audit carefully the plugins you allow to your users, in a sandboxed environnement
- Deploy your own plugin repository in which you control which plugin are available
- Take benefit of the advanced customization possibilities of QGIS to constraint settings around connexions, authentication etc..
- Don't focus only on code breaches, but also on user behavior regarding credentials and the risk of leak in project files if users insist on using basic authentication.  
 

### Do we affect Common Vulnerabilities and Exposures (CVE) ?  

Currently, QGIS project is **not** a CVE Numbering Authority (CNA), so we don't affect CVE identifiers. 


### Security Process

Disclosures are discussed in a private dedicated repository.

Fixes are shipped as soon as possible - regarding the criticity of the issue - in point releases. 




{{< content-end >}}
