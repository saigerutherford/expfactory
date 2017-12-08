# CHANGELOG

This is a manually generated log to track changes to the repository for each release. 
Each section should include general headers such as **Implemented enhancements** 
and **Merged pull requests**. All closed issued and bug fixes should be 
represented by the pull requests that fixed them. This log originated with Singularity 2.4
and changes prior to that are (unfortunately) done retrospectively. Critical items to know are:

 - renamed commands
 - deprecated / removed commands
 - changed defaults
 - backward incompatible changes (recipe file format? image file format?)
 - migration guidance (how to convert images?)
 - changed behaviour (recipe sections work differently)


## [v3.x](https://github.com/expfactory/expfactory/tree/headless) (development)

**additions**
 - this changelog was added
**changed defaults**
 - the interactive portal study identifier used to be an incrementing number. To be consistent with the ability to generate a token, the identifier is now an automatically generated 34 character string.

**features**
 - `--headless` has been added as an option for start, meaning that the portal is closed off and tokens must be entered to participate. The experiments order is either preset with `--experiments` and `--no-randomize`, randomized (default) or filtered to a limited subset (`--experiments` without `--no-randomize`),
 - `expfactory logs` can be used inside the container to print out application logs. With `--tail` they are left open for viewing updates.

## [v3.0](https://github.com/expfactory/expfactory/releases/tag/v3.0) (v3.0)

 - databases are added for filesystem, sqlite, postgres, and mysql. See [release notes](https://vsoch.github.io/2017/expfactory-beta/). Note that the 2.0 is equivalent to 3.0, minus the addition of the paper folder.
