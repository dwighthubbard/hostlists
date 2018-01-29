"""hostlists plugins class"""


class HostlistsPlugin(object):

    @property
    def names(self):
        return []

    def expand(self, value, name=None):
        return value
