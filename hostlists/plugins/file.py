#!/usr/bin/env python
""" hostlists plugin to get hosts from a file """
import os


def name():
    return ['file']


# noinspection PyUnusedLocal
def expand(value, name="file"):
    tmplist = []
    for host in [
        i.strip() for i in open(os.path.expanduser(value), 'r').readlines()
    ]:
        if not host.startswith('#') and len(host.strip()):
            tmplist.append(host)
    return tmplist
