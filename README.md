# giftwrap

Giftwrap server for 'malicious' packages in pip, gems, npm

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the None license.

## Two modes

1. Trashfire 
	* Backdoor a specific package, regardless of version, without serving the real package
			* May fail tests (most likely will)
			* Will cause outages and/or break functionality of real packages, alerting defenders/victims that something is wrong with the package
2. Paranoid
  * Shim malicious postinstall/freeze/develop command into a specific package, version, serve the real package with an overwritten/appended `setup.py`

## Attack chain / infection scenarios

1. Own/poison DNS and point pypi.org A record to giftwrap
2. Own CI/CD or build pipeline and specify giftwrap
   * https://docs.travis-ci.com/user/deployment/pypi/#releasing-to-a-self-hosted-pypi 
3. Environment variable fun stuff
  * https://pip.pypa.io/en/stable/user_guide/#environment-variables
	* `export PIP_EXTRA_INDEX_URL=http://localhost:8080/simple/`
4. `pip.conf` 
  * https://pip.pypa.io/en/stable/user_guide/#config-file

## Shimming
  * Generate dynamic sdist https://stackoverflow.com/a/35496354
  * pypi tomfoolery
  * parsesetup https://github.com/benfred/parsesetup/blob/effab26ec3d7aac89c70fbcdaa09b7cc028eda7d/parsesetup.py#L44
    * https://github.com/pypa/pip/blob/7ec0fa5142466f8402bb866a1dcfb8ca6ffdc66b/src/pip/_internal/utils/setuptools_build.py
  * potential: use build? https://github.com/pypa/build
