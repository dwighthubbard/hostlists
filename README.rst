=========
hostlists
=========

.. image:: https://travis-ci.org/yahoo/hostlists.svg?branch=master
    :target: https://travis-ci.org/yahoo/hostlists

.. image:: https://coveralls.io/repos/yahoo/hostlists/badge.svg
  :target: https://coveralls.io/r/yahoo/hostlists

    
Python module to generate lists of hosts from various sources that is extensible
via plugins.


Components
----------
hostlists has 2 components:

  * hostlists - This module handles hostlist expansion
  * hostlists_plugins - This module contains plugins that allow hostlists to get lists of hosts from various backend systems.


Dependencies
------------
  * dnspython (BSD License)
    This python module is used for the dns plugins to perform host expansion
    based on dns.


Usage
-----
The hostlists module provides a python module to do host expansion within python
programs.  It also provides a command line utility to allow usage from the
command line.


Creating Hostlists backend plugins
----------------------------------

TBD


Command Line Examples
---------------------
Expand a list of hosts from round robin dns using the dns plugin

.. code-block:: bash

    $ hostlists dns:www.google.com
    pb-in-f99.1e100.net, pb-in-f[103-106].1e100.net, pb-in-f147.1e100.net


Multiple hosts, ranges and plugins can be passed for a single hostlists

.. code-block:: bash

    $ hostlists dns:www.google.com, poodle[10-20,23].dog.com
    pb-in-f99.1e100.net, pb-in-f[103-106].1e100.net, pb-in-f147.1e100.net, poodle[10-20].dog.com, poodle23.dog.com
    
