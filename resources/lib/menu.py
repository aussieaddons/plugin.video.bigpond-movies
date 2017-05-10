import xbmcgui
import xbmcplugin
import sys
import utils
import comm

_handle = int(sys.argv[1])
_url = sys.argv[0]


def make_content_list(params):
    """ create list of playable movies/tv shows"""
    listing = []
    category = params['category']
    utils.log('Category is: {0}'.format(category))
    if category == 'episodes':
        content = comm.list_episodes(params['series_id'])
    elif category == 'movies':
        content = comm.list_movies()
    elif category == 'TV Shows':
        content = comm.list_tv_shows()
    elif category == 'Thanks Thursdays':
        content = comm.list_trailers('thanks')
    elif category == 'Featured':
        content = comm.list_trailers('featured')
    utils.log(category)
    for p in content:
        li = xbmcgui.ListItem(label=str(p.title), iconImage=p.thumb,
                              thumbnailImage=p.thumb)
        url = '{0}?action=list{1}{2}'.format(_url, category, p.make_kodi_url())
        is_folder = False
        li.setProperty('IsPlayable', 'true')
        li.setProperty('inputstreamaddon', 'inputstream.adaptive')
        li.addStreamInfo('video', p.get_stream_info())
        li.setInfo('video', p.get_info())
        li.setArt(p.get_art())
        listing.append((url, li, is_folder))

    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)


def list_series(params):
    """ list tv show series that have been purchased"""
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


def list_library(params):
    listing = []
    for item in ['Movies', 'TV Shows']:
        li = xbmcgui.ListItem(label=item)
        url = '{0}?action=librarylist&category={1}'.format(_url, item.lower())
        is_folder = True
        listing.append((url, li, is_folder))

    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)
