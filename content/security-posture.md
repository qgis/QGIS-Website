---
draft: true
---

When was the application last updated?
QGIS release cycle is publicly available at https://qgis.org/en/site/getinvolved/development/roadmap.html#release.
We do security releases each month for Long Term Version and Release version (with some variations during the release candidate phase). That means, you can act on QGIS's project and benefit from fixed versions. However, we have quarantine rules to ensure bugfixes are not triggering regressions.

How often is it updated?
Basically every month. Our long term version is maintained for 1 year when release version is maintained for 4 monthes.

Are there any guidance that is followed such as OWASP Application Security Verification Standards?
We have a public adress to collect security alerts at security@qgis.org. The we have a private repository to handle those issues. See https://github.com/qgis/QGIS/security/policy
We follow a classical CVE logic, by fixing issues and alerting in the changelog for security concerns. QGIS is however mainly a desktop tool with scripting abilities. It is then relying a lot more on the OS's and organizations security policies than a web server or a database server does.
We already have work funded by private companies to stress test QGIS server against security issues, mainly SQL injection.
Do you conform with a recognised security standard? (e.g., SOC1/2/3, ISO27001)
Nothing formal here no. But the gate is opened to go this way.  Every work implying administrative and recurrent job is however difficult to us. Any sponsorship in this area is more than welcome. The only certification process we apply for is the OGC compliancy process, to guarantee QGIS is following the implemented OGC standards.

Do you have an Information Security Policy with supporting Standards and Procedures? Please provide details (or provide a copy of the policy).
Nothing ready yet.
Do you have formal change control and release management processes to manage code changes? Please provide details (or provide a copy of the documented process).
Yes, QGIS is fully structured with code versionning and issue trackers for years. Source code, release practices, branches, tags, issues, are publicly available at https://github.com/qgis/

We have a massive continuous integration system with build tests, unit test, performance and compliancy tests.


Is the source code stored anywhere other than GitHub. If so where is and is it secure?
As a distributed git version, QGIS source code is mirrored on at least 2500 repositories on Github itself Each core dev has a copy of the code, making it pretty resilient to datalosses in cas GitHub would fail (we don't count other mirrors that also exists in gitlab instances for example)
Do you follow secure development processes? How is this achieved?
We have a strict pair review process, followed by continuous integration. I am not aware of an automatic code analyzer being run on QGIS source code. I'll ask dev's.
Are there any common vulnerabilities?
Most known CVE's we have report for are from depencies. QGIS is relying on a lot of libraries, like GDAL, python, many python libraries etc.. Our release manager reacts quickly for the distributions we officialy support, ie Windows and Debian/Ubuntu. For Windows, the project, this is handled in the dedicated repository (which is not only used by QGIS). See for instance this  ticket : https://trac.osgeo.org/osgeo4w/ticket/116
Is there a reporting process for reporting vulnerabilities and remediation processes? Please provide details/a copy of the documented process
The process is straight simple. Critical CVE should be raised via the mail address security@qgis.org . Other issues keep being collected via the main bugtracker, or official mailing lists.
Do you undertake audits or other reviews to ensure that security controls are being implemented and operating effectively? How is this done? Can you provide details of this?
We now have a yearly minimal budget to be able to react to severe and urgent issues.
More important work are usually funded and realized via the companies providing commercial support. See for instance such work done a while ago: https://oslandia.com/2017/06/14/qgis-server-security-aspect/
Do you undertake regular penetration testing (or similar technical security testing, code review or vulnerability assessment); and are you able to provide a summary of results/findings?
As for QGIS server, there is a daily server running security tests.
As for QGIS desktop, the penetration scenarios are not really defined, since they are desktop tools. When a scenario is defined we can implement unit tests that are run against every possible change with the CI chain.
Do your employees (e.g., developers or system administrators) have access to customer data? How is this access controlled and monitored?
QGIS is an open source and free project. QGIS.org does not collect any user data - except to server logs broadcasting newsfeed when QGIS is fired somewhere. 
Are all personnel required to sign Non-Disclosure Agreement (NDA) or Confidentiality Agreements (CA) as a condition of employment to protect customer information?
It is not relevant as QGIS.org is not a company and QGIS does not sends any customer data to a central entity.
Do you have Business Continuity and/or Disaster Recovery Plans? If Yes, please provide details including backup and redundancy mechanisms.
Again, QGIS.org infrastructure is not linked to anything users do with their data. If QGIS.org servers are down, this will not imply a disaster to QGIS users - except maybe for community plugins. 
Is there a  dedicated security team?
Yes, we have 11 persons in the list, including most core developpers.
Is there a contact for security issues?
security@qgis.org
Has a vulnerability disclosure program?
No
Is there a bug bounty program?
nothing from qgis.org
Does QGIS require third party authorization/connections?
No. QGIS is a database client able to connect to many datasources. Some require authorization. QGIS offers an encrypted password manager (funded by a US federal administration very concerned by security issues). This password manager can delegate password management to the OS's password manager.
