"""Fork of RaspiMote_https. It improves the web server, especially by adding verbose options. It is used as an HTTPS server in RaspiMote releases."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('raspimote_https').version
except Exception:
    __version__ = 'unknown'
