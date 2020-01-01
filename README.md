[![Build Status](https://cd.screwdriver.cd/pipelines/3816/badge?nocache=true)](https://cd.screwdriver.cd/pipelines/3816)
[![Package](https://img.shields.io/badge/package-pypi-blue.svg)](https://pypi.org/project/screwdrivercd/)
[![Downloads](https://img.shields.io/pypi/dm/hostlists.svg)](https://img.shields.io/pypi/dm/hostlists.svg)
[![Codecov](https://codecov.io/gh/yahoo/hostlists/branch/master/graph/badge.svg?nocache=true)](https://codecov.io/gh/yahoo/hostlists)
[![Codestyle](https://img.shields.io/badge/code%20style-pep8-blue.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Documentation](https://img.shields.io/badge/Documentation-latest-blue.svg)](https://yahoo.github.io/hostlists/)

---

# hostlists

Python module to generate lists of hosts from various sources that is extensible
via plugins.


## Components

hostlists has 2 components:

- hostlists - This module handles hostlist expansion
- hostlists_plugins - This module contains plugins that allow hostlists to get lists of hosts from various backend systems.


## Dependencies

- dnspython (BSD License) - This python module is used for the dns plugins to perform host expansion based on dns.


## Usage

The hostlists module provides a python module to do host expansion within python
programs.  It also provides a command line utility to allow usage from the
command line.

## Command Line Examples

Expand a list of hosts from round robin dns using the dns plugin

```bash
$ hostlists dns:www.google.com
pb-in-f99.1e100.net, pb-in-f[103-106].1e100.net, pb-in-f147.1e100.net
```


Multiple hosts, ranges and plugins can be passed for a single hostlists

```bash
    $ hostlists dns:www.google.com, poodle[10-20,23].dog.com
    pb-in-f99.1e100.net, pb-in-f[103-106].1e100.net, pb-in-f147.1e100.net, poodle[10-20].dog.com, poodle23.dog.com
```
