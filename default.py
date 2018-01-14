import os
import sys
import xbmc
import xbmcgui
import xbmcaddon
import drmhelper
from urlparse import parse_qsl

addon = xbmcaddon.Addon()
cwd = xbmc.translatePath(addon.getAddonInfo('path')).decode("utf-8")
BASE_RESOURCE_PATH = os.path.join(cwd, 'resources', 'lib')
sys.path.append(BASE_RESOURCE_PATH)

import telstra_auth  # noqa: E402
import play  # noqa: E402
import menu  # noqa: E402
from aussieaddonscommon import utils  # noqa: E402

_url = sys.argv[0]
_handle = int(sys.argv[1])
addonname = addon.getAddonInfo('name')
addonPath = xbmcaddon.Addon().getAddonInfo("path")
fanart = os.path.join(addonPath, 'fanart.jpg')


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring
    :param paramstring:
    """
    params = dict(parse_qsl(paramstring))
    utils.log('Running addon with params: {0}'.format(params))
    if paramstring:
        if paramstring != 'content_type=video':
            if params['action'] == 'listcategories':
                if params['category'] == 'My Library':
                    menu.list_library(params)
                elif params['category'] == 'Settings':
                    addon.openSettings()
                else:
                    menu.make_content_list(params)
            elif params['action'] == 'librarylist':
                if params['category'] == 'movies':
                    menu.make_content_list(params)
                elif params['category'] == 'tv shows':
                    menu.list_series(params)
            elif params['action'] == 'listseries':
                menu.make_content_list(params)
            elif params['action'] == 'listplayable':
                play.play_video(params)
            elif params['action'] == 'cleartoken':
                telstra_auth.clear_token()
            elif params['action'] == 'reinstall_widevine_cdm':
                drmhelper.get_widevinecdm()
            elif params['action'] == 'reinstall_ssd_wv':
                drmhelper.get_ssd_wv()
    else:
        menu.list_categories()


if __name__ == '__main__':
    if addon.getSetting('firstrun') == 'true':
        xbmcgui.Dialog().ok(addonname, ('Please enter your Telstra ID '
                                        'username and '
                                        'password to access the content in '
                                        'this service.'))
        addon.openSettings()
        addon.setSetting('firstrun', 'false')
    xbmc.log(sys.argv[2][1:])
    router(sys.argv[2][1:])
