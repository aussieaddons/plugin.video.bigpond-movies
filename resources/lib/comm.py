import classes
import utils
import config
import requests
import json
import telstra_auth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# Ignore InsecureRequestWarning warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
session = requests.Session()
session.verify = False
session.mount("https://", classes.TLSv1Adapter(max_retries=5))


def list_movies():
    data = get_url(config.QUERY_URL.format('mylibrary'))
    listing = []
    movies = data['content'].get('movies')
    for item in movies.get('purchases') + movies.get('rentals'):
        p = classes.movie()
        p.title = utils.ensure_ascii(item.get('name'))
        p.desc = item.get('shortSynopsis')
        p.thumb = item['images'].get('slickUrl')
        p.fanart = item['images'].get('keyartUrl')
        if item['renditions'].get('isHD') is True:
            p.qual = 'HD'
        else:
            p.qual = 'SD'
        for rendition in item['renditions']['consume']:
            if rendition.get('renditionType') == p.qual:
                p.video_id = rendition.get('embedCode')
        listing.append(p)
    return listing


def list_tv_shows():
    data = get_url(config.QUERY_URL.format('mylibrary'))
    listing = []
    series = data['content'].get('series')
    for item in series.get('purchases') + series.get('rentals'):
        p = classes.movie()
        p.title = utils.ensure_ascii(item.get('name'))
        p.desc = item.get('shortSynopsis')
        p.thumb = item['images'].get('slickUrl')
        p.fanart = item['images'].get('keyartUrl')
        p.series_id = item.get('id')
        listing.append(p)
    return listing


def list_episodes(asset):
    data = get_url(config.SERIES_URL.format(asset))
    listing = []
    series = data['content'].get('buttons')
    for item in series:
        for x in series[item]:
            if x.get('type') == 'play':
                p = classes.movie()
                p.title = x['consume'][0].get('assetName')
                p.title += ' ' + x['consume'][0].get('renditionType')
                p.video_id = x['consume'][0].get('embedCode')
                p.qual = 'SD'  # need to get actual value
                listing.append(p)
    return listing


def list_trailers(category):
    """ go through our xml file and retrive all we need to pass to kodi"""
    data = get_url(config.QUERY_URL.format(category))
    listing = []
    x = 0
    for asset_list in data.get('content'):
        for item in asset_list.get('assets'):
            if item.get('type') != 'movie':
                break
            p = classes.movie()
            get_metadata(p, item)
            listing.append(p)
            x += 1
            if x > 20:
                break
        if x > 20:
            break
    return listing


def get_url(url):
    """ retrieve our json file for processiqng"""
    telstra_auth.get_user_token(session)
    utils.log('Fetching URL: {0}'.format(url))
    res = session.get(url)
    return json.loads(res.text)


def get_metadata(p, item):
    p.title = utils.ensure_ascii(item.get('name'))
    p.shortdesc = item.get('shortSynopsis')
    p.longdesc = item.get('longSynopsis')
    p.thumb = item['images'].get('slickUrl')
    p.fanart = item['images'].get('keyartUrl')
    p.genre = item.get('genres')
    p.director = item.get('directors')
    p.duration = item.get('duration')
    p.year = item.get('productionYear')
    p.cast = item.get('actors')
    for rendition in item['renditions']['consume']:
        if rendition.get('renditionType') == 'Trailer':
            p.video_id = rendition.get('embedCode')
        if rendition.get('renditionType') == 'HD':
            p.qual = 'HD'
