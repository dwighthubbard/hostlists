from __future__ import print_function
import argparse
import sys
from .range import compress, expand, range_split
from .plugin_manager import installed_plugins


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'host_range', nargs='*', type=str, help='plugin:parameters'
    )
    parser.add_argument(
        "-s", "--sep",
        dest="sep",
        type=str,
        default='',
        help="Separator character, default=\",\""
    )
    parser.add_argument(
        "--onepass",
        dest="onepass",
        default=False,
        action="store_true",
        help="Only perform a single expansion pass (no recursion)"
    )
    parser.add_argument(
        "--expand", "-e",
        dest="expand",
        default=False,
        action="store_true",
        help="Expand the host list and display one host per line"
    )
    parser.add_argument(
        "--list_plugins", "-l",
        dest="list_plugins",
        default=False,
        action="store_true",
        help="List the currently found hostlists plugins"
    )
    result = parser.parse_args()
    if result.expand:
        if not result.sep:
            result.sep = '\n'
    else:
        if not result.sep:
            result.sep = ','
    return result


def main():  # pragma: no cover
    options = parse_arguments()
    if options.list_plugins:
        plugins = installed_plugins()
        plugins.sort()
        print(
            'Hostlists plugins currently installed are:'
        )
        print('\t' + '\n\t'.join(plugins))
        return

    hostnames = range_split(','.join(options.host_range))
    seperator = options.sep + ' '
    if options.expand:
        print(options.sep.join(expand(hostnames, onepass=options.onepass)))
    else:
        print(
            seperator.join(
                compress(
                    expand(
                        hostnames, onepass=options.onepass
                    )
                )
            ).strip().strip(',').strip()
        )
