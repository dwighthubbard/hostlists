# Copyright (c) 2012-2015, Yahoo Inc.
# Copyrights licensed under the Apache 2.0 License
# See the accompanying LICENSE.txt file for terms.
"""
This module is a plugin extensible module to generate lists of hosts
from various sources.

Attributes:
    __version__(str):
        The version of the yahoo_boss module.

    __redis_executable__(str):
        The full path to the embedded redis-server executable.

    __redis_server_version__(str):
        The version of the embedded redis-server built intot he module.

    __git_source_url__(str):
        The github web url for the source code used to generate this module.
        This will be an empty string if the module was not built from a github
        repo.

    __git_version__(str):
        Version number derived from the number of git revisions.
        This will be an empty string if not built from a git repo.

    __git_origin__(str):
        The git origin of the source repository the module was built from.
        This will be an empty string if not built from a git repo.

    __git_branch__(str):
        The git branch the module was built from.  This will be an empty string
        if not built from a git repo.

    __git_hash__(str):
        The git hash value for the code used to build this module.
"""
import json
import os


_metadata_file = os.path.join(
    os.path.dirname(__file__),
    'package_metadata.json'
)

if os.path.exists(_metadata_file):  # pragma: no cover
    with open(_metadata_file) as _file_handle:
        _package_metadata = json.load(_file_handle)
else:
    _package_metadata = {
        'version': '0.0.0'
    }

__version__ = str(_package_metadata.get('version', '0.0.0'))
__git_version__ = str(_package_metadata.get('git_version', ''))
__ci_version__ = str(_package_metadata.get('ci_version', ''))
__ci_build_number__ = str(_package_metadata.get('ci_build_number', ''))
__git_branch__ = str(_package_metadata.get('git_branch', ''))
__git_origin__ = str(_package_metadata.get('git_origin', ''))
__git_hash__ = str(_package_metadata.get('git_hash', ''))
__git_base_url__ = 'https://github.com/yahoo/hostlists'
__source_url__ = __git_base_url__ + '/tree/' + __git_hash__

from .hostlists import compress, compress_domain, expand, expand_item   # NOQA
from .hostlists import global_plugins, installed_plugins, multiple_names  # NOQA
from .hostlists import range_split, get_setting, HostListsError  # NOQA
from .hostlists import get_plugins, cmp_compat  # NOQA
