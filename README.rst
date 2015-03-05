=========
hostlists
=========

.. image:: https://travis-ci.org/yahoo/hostlists.svg?branch=master
    :target: https://travis-ci.org/yahoo/hostlists
    
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

## Expand a list of hosts from round robin dns using the hosts plugin

.. code-block:: shell

    $ hostlists dns:www.google.com
    pb-in-f99.1e100.net, pb-in-f[103-106].1e100.net, pb-in-f147.1e100.net

