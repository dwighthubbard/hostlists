import imp
import logging
import os
import sys
import pkg_resources
from .exceptions import HostListsError
from .plugin_base import HostlistsPlugin


# Global plugin cache so we don't constantly reload the plugin modules
global_plugins = {}
pkg_resources_probed = False
plugins_probed = False


logger = logging.getLogger(__name__)


def _get_plugins__pkg_resources():
    """Query pkg_resources for packages that registered with the plugin entrypoint"""
    global global_plugins
    global pkg_resources_probed
    if pkg_resources_probed:
        return global_plugins
    entry_points = pkg_resources.iter_entry_points(group='hostlists_plugins')
    if not entry_points:
        return global_plugins
    for entry_point in entry_points:
        plugin_class = entry_point.load()
        for name in plugin_class.names:
            global_plugins[name] = plugin_class()
    pkg_resources_probed = True
    return global_plugins


def _get_plugins():
    """ Find all the hostlists plugins """
    global global_plugins
    global plugins_probed

    if plugins_probed:
        return global_plugins

    plugins = _get_plugins__pkg_resources()

    pluginlist = []
    plugin_path = [
        '/home/y/lib/hostlists',
        os.path.dirname(__file__),
        '~/.hostlists',
    ] + sys.path
    for directory in plugin_path:
        if os.path.isdir(os.path.join(directory, 'plugins')):
            templist = os.listdir(os.path.join(directory, 'plugins'))
            for item in templist:
                pluginlist.append(
                    os.path.join(os.path.join(directory, 'plugins'), item)
                )
    pluginlist.sort()
    # Create a dict mapping the plugin name to the plugin method
    for item in pluginlist:
        if item.endswith('.py'):
            module_file = open(item)
            try:
                mod = imp.load_module(
                    'hostlists_plugins_%s' % os.path.basename(item[:-3]),
                    module_file,
                    item,
                    ('.py', 'r', imp.PY_SOURCE)
                )
                names = mod.name()
                if isinstance(names, str):
                    names = [names]
                for name in names:
                    if name not in plugins.keys():
                        plugins[name.lower()] = mod
            except (AttributeError, ImportError):
                # Error in module import, probably a plugin bug
                logger.debug(
                    "Plugin import failed %s:" % item
                )
            if module_file:
                module_file.close()
    plugins_probed = True
    return plugins


def get_plugins():
    """ Wrap the get_plugins() function so it can be used by plugins"""
    return _get_plugins()


def run_plugin_expand(name, value):
    """
    Run a plugin's expand method
    """
    plugins = _get_plugins()
    if name not in plugins.keys():
        raise HostListsError(
            'plugin %s not found, valid plugins are: %s' % (
                name, ','.join(plugins.keys())
            )
        )
    logger.debug(plugins[name])
    logger.debug(dir(plugins[name]))
    return plugins[name].expand(value, name=name)


def installed_plugins():
    plugins = []
    for plugin in _get_plugins():
        if plugin:
            plugins.append(plugin)
    return plugins
