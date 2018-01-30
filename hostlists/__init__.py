# Copyright (c) 2012-2015 Yahoo! Inc. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. See accompanying LICENSE file.

__all__ = ['cli', 'decorators', 'exceptions', 'plugin_base', 'plugin_manager', 'range']
__version__ = '0.0.0dev0'


import json
import os
from .plugin_manager import get_plugins, installed_plugins, multiple_names, run_plugin_expand
from .range import compress, expand
from .range import range_split
from .exceptions import HostListsError


# Config file
CONF_FILE = os.path.expanduser('~/.hostlists.conf')


def get_setting(key):
    """
    Get setting values from CONF_FILE
    :param key:
    :return:
    """
    try:
        with open(CONF_FILE) as cf:
            settings = json.load(cf)
    except IOError:
        return None
    if key in settings.keys():
        return settings[key]
    return None    # pragma: no cover


try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution("hostlists").version
except (ImportError, pkg_resources.DistributionNotFound):
    pass
