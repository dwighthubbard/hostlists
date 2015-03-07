#!/usr/bin/env python
"""
A plugin extendable hostlist infrastructure

This module provides functions for getting a list of hosts
from various systems as well as compressing the list into
a simplified list.

This module uses the hostlists_plugins python scripts
to actually obtain the listings.
"""

# Copyright (c) 2010-2015 Yahoo! Inc. All rights reserved.
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


import errno
import os
import signal
from functools import wraps


class MethodTimeoutError(Exception):
    """
    Timeout exception class
    """
    pass


def timeout(seconds=300, error_message=os.strerror(errno.ETIME)):
    """
    Time out the function after a period of time
    :param seconds:
    :param error_message:
    :return:
    """
    def timeout_decorator(func):
        """
        Decorator function
        """
        def _handle_timeout(signum, frame):
            raise MethodTimeoutError(error_message)

        def timeout_wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(timeout_wrapper)
    return timeout_decorator
