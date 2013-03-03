Description
Hostlists is a python module and command line utility that handles
getting lists of hosts from various systems and syntaxes.  Hostlists
supports plugins allowing additional backend support to be added.

hostlists has 2 components:
  hostlists - This module handles hostlist expansion
  hostlists_plugins - This module contains plugins that can be used
                      by hostlists to obtain lists of hosts. 

Dependencies
  django - This provides the temlating engine used by some plugins.
           Django is provided under the BSD license.
