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

import pkg_resources
from .hostlists import cmp_compat, compress, compress_domain, expand, expand_item   # NOQA
from .plugin_manager import get_plugins, global_plugins, installed_plugins  # NOQA
from .hostlists import multiple_names, range_split, get_setting, HostListsError  # NOQA


__version__ = '0.0.0unknown0'
try:
    __version__ = pkg_resources.get_distribution("hostlists").version
except pkg_resources.DistributionNotFound:
    pass
