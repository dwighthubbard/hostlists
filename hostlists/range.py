"""hostlists range management functions"""
import operator
import re
from .plugin_manager import run_plugin_expand


# A list of operators we use for set options
SET_OPERATORS = ['-']


def cmp_compat(a, b):
    """
    Simple comparison function
    :param a:
    :param b:
    :return:
    """
    return (a > b) - (a < b)


def compress(hostnames):
    """
    Compress a list of host into a more compact range representation
    """
    domain_dict = {}
    result = []
    for host in hostnames:
        if '.' in host:
            domain = '.'.join(host.split('.')[1:])
        else:
            domain = ''
        try:
            domain_dict[domain].append(host)
        except KeyError:
            domain_dict[domain] = [host]
    domains = list(domain_dict.keys())
    domains.sort()
    for domain in domains:
        hosts = compress_domain(domain_dict[domain])
        result += hosts
    return result


def compress_domain(hostnames):
    """
    Compress a list of hosts in a domain into a more compact representation
    """
    hostnames.sort()
    prev_dict = {'prefix': "", 'suffix': '', 'number': 0}
    items = []
    items_block = []
    new_hosts = []
    for host in hostnames:
        try:
            parsed_dict = re.match(
                r"(?P<prefix>[^0-9]+)(?P<number>\d+)(?P<suffix>.*).?",
                host
            ).groupdict()
            # To generate the range we need the entries sorted numerically
            # but to ensure we don't loose any leading 0s we don't want to
            # replace the number parameter that is a string with the leading
            # 0s.
            parsed_dict['number_int'] = int(parsed_dict['number'])
            new_hosts.append(parsed_dict)
        except AttributeError:
            if '.' not in host:
                host += '.'
                parsed_dict = {'host': compress([host])[0].strip('.')}
            else:
                parsed_dict = {'host': host}
            new_hosts.append(parsed_dict)
    new_hosts = multikeysort(new_hosts, ['prefix', 'number_int'])
    for parsed_dict in new_hosts:
        if 'host' in parsed_dict.keys() or \
                parsed_dict['prefix'] != prev_dict['prefix'] or \
                parsed_dict['suffix'] != prev_dict['suffix'] or \
                int(parsed_dict['number']) != int(prev_dict['number']) + 1:
            if len(items_block):
                items.append(items_block)
            items_block = [parsed_dict]
        else:
            items_block.append(parsed_dict)
        prev_dict = parsed_dict
    items.append(items_block)
    result = []
    for item in items:
        if len(item):
            if len(item) == 1 and 'host' in item[0].keys():
                result.append(item[0]['host'])
            elif len(item) == 1:
                result.append(
                    '%s%s%s' % (
                        item[0]['prefix'], item[0]['number'], item[0]['suffix']
                    )
                )
            else:
                result.append(
                    '%s[%s-%s]%s' % (
                        item[0]['prefix'],
                        item[0]['number'],
                        item[-1]['number'],
                        item[0]['suffix']
                    )
                )
    return result


def multikeysort(items, columns):
    comparers = [
        ((operator.itemgetter(col[1:].strip()), -1) if col.startswith('-') else (operator.itemgetter(col.strip()), 1)) for col in columns
    ]

    def comparer(left, right):
        for fn, mult in comparers:
            try:
                result = cmp_compat(fn(left), fn(right))
            except KeyError:
                return 0
            if result:
                return mult * result
        else:
            return 0
    try:
        # noinspection PyArgumentList
        return sorted(items, cmp=comparer)
    except TypeError:
        # Python 3 removed the cmp parameter
        import functools
        return sorted(items, key=functools.cmp_to_key(comparer))


def range_split(hosts):
    """
    Split up a range string, this needs to separate comma separated
    items unless they are within square brackets and split out set operations
    as separate items.
    """
    in_brackets = False
    current = ""
    result_list = []
    for c in hosts:
        if c in ['[']:
            in_brackets = True
        if c in [']']:
            in_brackets = False
        if not in_brackets and c == ',':
            result_list.append(current)
            current = ""
        # elif not in_brackets and c == '-':
        #     result_list.append(current)
        #     result_list.append('-')
        #     current = ""
        elif not in_brackets and c in [','] and len(current) == 0:
            pass
        else:
            current += c
    current = current.strip().strip(',')
    if current:
        result_list.append(current)
    return result_list


def expand(range_list, onepass=False):
    """
    Expand a list of lists and set operators into a final host lists
    >>> expand(['foo[01-10]','-','foo[04-06]'])
    ['foo09', 'foo08', 'foo07', 'foo02', 'foo01', 'foo03', 'foo10']
    >>>
    """
    if isinstance(range_list, str):  # pragma: no cover
        range_list = [h.strip() for h in range_list.split(',')]
    new_list = []
    set1 = None
    operation = None
    for item in range_list:
        if set1 and operation:
            set2 = expand_item(item)
            new_list.append(list(set(set1).difference(set(set2))))
            set1 = None
            operation = None
        elif item in SET_OPERATORS and len(new_list):
            set1 = new_list.pop()
            operation = item
        else:
            expanded_item = expand_item(item, onepass=onepass)
            new_list.append(expanded_item)
    new_list2 = []
    for item in new_list:
        new_list2 += item
    return new_list2


def expand_item(range_list, onepass=False):
    """ Expand a list of plugin:parameters into a list of hosts """

    if isinstance(range_list, str):
        range_list = [range_list]

    # Iterate through our list
    newlist = []
    found_plugin = False
    for item in range_list:
        # Is the item a plugin
        temp = item.split(':')
        found_plugin = False
        if len(temp) > 1:
            plugin = temp[0].lower()
            # Do we have a plugin that matches the passed plugin
            newlist += run_plugin_expand(plugin, ':'.join(temp[1:]).strip(':'))
            found_plugin = True
        else:
            # Default to running through the range plugin
            newlist += run_plugin_expand('range', temp[0])

    # Recurse back through ourselves incase a plugin returns a value that
    # needs to be parsed
    # by another plugin.  For example a dns resource that has an address that
    # points to a load balancer vip that may container a number of hosts that
    # need to be looked up via the load_balancer plugin.
    if found_plugin and not onepass:
        newlist = expand_item(newlist)
    return newlist
