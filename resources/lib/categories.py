import xbmcgui
import xbmcplugin
import config
import sys

_handle = int(sys.argv[1])
_url = sys.argv[0]


def list_categories():
    listing = []
    
    for category in config.CATEGORIES:
        li = xbmcgui.ListItem(category)
        urlString = '{0}?action=listcategories&category={1}'
        url = urlString.format(_url, category)
        is_folder = True
        listing.append((url, li, is_folder))

    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)
