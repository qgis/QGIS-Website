---
type: "page"
title: "Road Map"
draft: false
HasBanner: false
sidebar: true
---
{{< content-start  >}}

# Road Map

Releases and development of QGIS follow a timebased schedule (roadmap).

- Even version numbers (2.18, 3.2 etc) are release versions.
    
- Odd version numbers (2.99, 3.1 etc) are development versions.
    

A new release will happen every four months. In the first three months, new development is taking place. In the last month before a release, a feature freeze is invoked and the final month is used for testing, bugfixing, translation and release preparations. When the release happens, a branch with an even release number is created and the master branch advances to the next odd version. After the release a call for packaging is issued.

Every third release (starting with 2.8) is a long-term-release (LTR) that is maintained until the next long-term-release occurs.

## Development phase

In the development phase, developers work on adding new features for the next release. Early adopters can use the nightly builds we have for all major platforms to see the development progress, do preliminary testing and provide bug reports and their thoughts to help with development.

## Feature freeze

In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

In the feature freeze, **developers** monitor the bugtracker and start working on fixing the reported issues and update the **visual changelog** with the features they added.

With the start of the feature freeze, the translation files will be updated so that **translators** can start their work. Note that this might be an incremental process as although the features are frozen, bug fixes might still introduce translation string changes.

Two weeks before the release, a hard freeze is initiated after which only fixes to severe problems and regressions introduced after the feature freeze are allowed in.

The release manager announces this on feature freeze.

## Release

On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

The packagers are notified that packaging can begin.

Once some packages are available the release can be announced and the website is updated accordingly.

## Release schedule

The schedule is aligned to produce roughly the same dates for each year given our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch branch, if there are backports. Beginning with the 3.28 release point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).

Schedule

TODO: should be generated from CSV

|Event|Latest|Long-Term Repo|Freeze|Date|Week #|Weeks|
|---|---|---|---|---|---|---|
|LTR/PR|3.28.0|3.22.12||2022-10-21|43|4|
|PR|3.28.1|3.22.13||2022-11-18|47|4|
|PR|3.28.2|3.22.14||2022-12-16|51|6|
|PR/FF|3.28.3|3.22.15|3.29|2023-01-27|5|5|
|EPR||3.22.16||2023-02-03|6||
|LR/PR|3.30.0|3.28.4||2023-03-03|10|4|
|PR|3.30.1|3.28.5||2023-03-31|14|4|
|PR|3.30.2|3.28.6||2023-04-28|18|4|
|PR/FF|3.30.3|3.28.7|3.31|2023-05-26|22|4|
|LR/PR|3.32.0|3.28.8||2023-06-23|26|4|
|PR|3.32.1|3.28.9||2023-07-21|30|4|
|PR|3.32.2|3.28.10||2023-08-18|34|4|
|PR/FF|3.32.3|3.28.11|3.33|2023-09-15|38|6|
|LTR/PR|3.34.0|3.28.12||2023-10-27|44|4|
|PR|3.34.1|3.28.13||2023-11-24|48|4|
|PR|3.34.2|3.28.14||2023-12-22|52|4|
|PR/FF|3.34.3|3.28.15|3.35|2024-01-19|3|5|
|LR/PR|3.36.0|3.34.4||2024-02-23|8|4|
|PR|3.36.1|3.34.5||2024-03-22|12|4|
|PR|3.36.2|3.34.6||2024-04-19|16|4|
|PR/FF|3.36.3|3.34.7|3.37|2024-05-17|20|5|
|LR/PR|3.38.0|3.34.8||2024-06-21|25|4|
|PR|3.38.1|3.34.9||2024-07-19|29|4|
|PR|3.38.2|3.34.10||2024-08-16|33|4|
|PR/FF|3.38.3|3.34.11|3.39|2024-09-13|37|6|
|LTR/PR|3.40.0|3.34.12||2024-10-25|43|4|
|PR|3.40.1|3.34.13||2024-11-22|47|4|
|PR|3.40.2|3.34.14||2024-12-20|51|4|
|PR/FF|3.40.3|3.34.15|3.41|2025-01-17|3|5|
|LR/PR|3.42.0|3.40.4||2025-02-21|8|4|
|PR|3.42.1|3.40.5||2025-03-21|12|4|
|PR|3.42.2|3.40.6||2025-04-18|16|4|
|PR/FF|3.42.3|3.40.7|3.43|2025-05-16|20|5|
|LR/PR|3.44.0|3.40.8||2025-06-20|25|4|
|PR|3.44.1|3.40.9||2025-07-18|29|4|
|PR|3.44.2|3.40.10||2025-08-15|33|4|
|PR/FF|3.44.3|3.40.11|3.45|2025-09-12|37|6|
|LTR/PR|3.46.0|3.40.12||2025-10-24|43|4|
|PR|3.46.1|3.40.13||2025-11-21|47|4|
|PR|3.46.2|3.40.14||2025-12-19|51|4|
|PR/FF|3.46.3|3.40.15||2026-01-16|3|5|

Event legend
|Event|Description|
|---|---|
|LTR|Long term release, begin of new development phase|
|LR|Regular release, begin of new development phase|
|FF|Feature freeze, end of development phase|
|PR|Point release of latest release and LTR branch|
|EPR|Extra Point release|
|current|currently supported releases: 3.28.15 and 3.34.3|
|next|next releases|

## Location of prereleases / nightly builds {#qgis-prereleases}

|Platform|Location|
|---|---|
|Windows|[OSGeo4W]({{< ref "resources/installation-guide#osgeo4w-installer" >}})|
|Linux|[Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}})|
|MacOS|[Mac OS]({{< ref "resources/installation-guide#qgis-nightly-release" >}})|

{{< content-end >}}
