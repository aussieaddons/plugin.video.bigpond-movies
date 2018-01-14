import xbmcgui
import xbmcplugin
import sys
import comm
import config

from aussieaddonscommon import utils

_handle = int(sys.argv[1])
_url = sys.argv[0]


def list_categories():
    try:
        listing = []
        for category in config.CATEGORIES:
            li = xbmcgui.ListItem(category)
            urlString = '{0}?action=listcategories&category={1}'
            url = urlString.format(_url, category)
            is_folder = True
            listing.append((url, li, is_folder))

        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)
    except Exception:
        utils.handle_error('Unable to list categories')


def make_content_list(params):
    """ create list of playable movies/tv shows"""
    try:
        listing = []
        category = params['category']
        if category == 'episodes':
            content = comm.list_episodes(params['series_id'])
        elif category == 'movies':
            content = comm.list_movies()
        elif category == 'Thanks Thursdays Trailers':
            content = comm.list_trailers('thanks')
        elif category == 'Featured Movie Trailers':
            content = comm.list_trailers('featured')
        for p in content:
            li = xbmcgui.ListItem(label=str(p.title), iconImage=p.thumb,
                                  thumbnailImage=p.thumb)
            url = '{0}?action=listplayable{1}'.format(_url, p.make_kodi_url())
            is_folder = False
            li.setProperty('IsPlayable', 'true')
            li.setProperty('inputstreamaddon', 'inputstream.adaptive')
            li.addStreamInfo('video', p.get_stream_info())
            li.setInfo('video', p.get_info())
            li.setArt(p.get_art())
            listing.append((url, li, is_folder))

        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)
    except Exception:
        utils.handle_error('Unable to list content')


def list_series(params):
    """ list tv show series that have been purchased"""
    try:
        listing = []
        content = comm.list_tv_shows()

        for p in content:
            li = xbmcgui.ListItem(label=str(p.title), iconImage=p.thumb,
                                  thumbnailImage=p.thumb)
            url = '{0}?action=listseries{1}&category=episodes'.format(
                _url, p.make_kodi_url())
            is_folder = True
            li.setArt(p.get_art())
            listing.append((url, li, is_folder))

        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)
    except Exception:
        utils.handle_error('Unable to list tv series')


def list_library(params):
    try:
        listing = []
        for item in ['Movies', 'TV Shows']:
            li = xbmcgui.ListItem(label=item)
            url = '{0}?action=librarylist&category={1}'.format(_url,
                                                               item.lower())
            is_folder = True
            listing.append((url, li, is_folder))

        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)
    except Exception:
        utils.handle_error('Unable to list library')
