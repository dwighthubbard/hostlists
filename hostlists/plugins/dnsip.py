#!/usr/bin/env python
""" hostlists plugin to get hosts from dns """

__license__ = """
 Copyright (c) 2012-2014 Yahoo! Inc. All rights reserved.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,   
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License. See accompanying LICENSE file.
"""
import dns.resolver


def name():
    return 'dnsip'


def expand(value):
    tmplist = []
    try:
        answers = list(dns.resolver.query(value))
    except dns.resolver.NoAnswer:
        answers = []
    for rdata in answers:
        tmplist.append(rdata.address)
    return tmplist
  