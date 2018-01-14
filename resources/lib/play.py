import ooyalahelper
import sys
import xbmcaddon
import xbmcgui
import xbmcplugin

from aussieaddonscommon import utils

addon = xbmcaddon.Addon()
_handle = int(sys.argv[1])


def play_video(params):
    """
    Play a video by the provided path.
    :param path: str
    """
    if 'dummy' in params:
        if params['dummy'] == 'True':
            return
    try:
        import drmhelper
        if drmhelper.check_inputstream():
            dash_stream = ooyalahelper.get_dash_playlist(params['video_id'])
            url = dash_stream['dash_url']
            play_item = xbmcgui.ListItem(path=url)
            play_item.setProperty('inputstream.adaptive.manifest_type', 'mpd')
            play_item.setProperty(
                'inputstream.adaptive.license_type', 'com.widevine.alpha')
            play_item.setProperty(
                'inputstream.adaptive.license_key',
                dash_stream['wv_lic']+('|Content-Type=application%2F'
                                       'x-www-form-urlencoded|A{SSM}|'))
            xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)
        else:
            xbmcplugin.setResolvedUrl(_handle, True,
                                      xbmcgui.ListItem(path=None))
            return

    except Exception:
        utils.handle_error('Unable to play video')
