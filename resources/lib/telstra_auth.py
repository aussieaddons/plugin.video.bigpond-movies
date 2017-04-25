import requests
import json
import urlparse
import urllib
import config
import re
import ssl
import utils
import classes
import time
import xbmcaddon
import xbmcgui
try:
    import StorageServer
except:
    from storageserverdummy import StorageServer
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from requests.packages.urllib3.exceptions import InsecureRequestWarning



# Ignore InsecureRequestWarning warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
cache = StorageServer.StorageServer(config.ADDON_ID, 1)
addon = xbmcaddon.Addon()





def clear_token():
    """Remove stored token from cache storage"""
    cache.delete('BIGPONDTOKEN')
    cache.delete('BIGPONDCOOKIES')


def get_new_token(session):
    """send user login info and retrieve token for session"""
    utils.log('Retrieving new user token')
    username = addon.getSetting('LIVE_USERNAME')
    password = addon.getSetting('LIVE_PASSWORD')

    session.headers = config.BIGPOND_HEADERS
    #session.cookies.update(json.loads(cookies))
    #session.headers = config.APIGEE_HEADERS

    url = config.BIGPOND_URL.format(username, password)
    auth_resp = session.post(url)  # make sure not to log this!!
    auth_json = json.loads(auth_resp.text)
    artifact = auth_json['data'].get('artifactValue')
    
    session.headers = config.APIGEE_HEADERS
    url = config.APIGEE_URL.format(urllib.quote(artifact))
    token_resp = session.get(url)
    try:
        token_resp.raise_for_status()
    except requests.HTTPError as e:
        raise e
    token = json.loads(token_resp.text)
    session.headers.update({'ovs-token': token.get('tokenId'),
                            'ovs-uuid': token.get('uuid')})

    cookies = json.dumps(session.cookies.get_dict())
    expire = datetime.now() + timedelta(hours=2)
    cache.set('BIGPONDTOKEN', json.dumps(token))
    cache.set('BIGPONDCOOKIES', cookies)
    cache.set('BIGPONDEXPIRE', str(expire))
    return token


def get_user_token(session):
    """Check storage cache for valid token"""
    stored_token = cache.get('BIGPONDTOKEN')
    str_expire = cache.get('BIGPONDEXPIRE')
    utils.log('expire: {0}'.format(str_expire))
    if not stored_token or not str_expire:
        utils.log('No stored token')
        token = get_new_token(session)
    else:
        format = '%Y-%m-%d %H:%M:%S.%f'
        # workaround for weird python bug
        try:
            expire = datetime.strptime(str_expire, format)
        except TypeError:
            expire = datetime(*(time.strptime(str_expire, format)[0:6]))
        if expire <= datetime.now():
            utils.log('Stored token expired')
            token = get_new_token(session)
        else:
            utils.log('Using stored token')
            token = json.loads(stored_token)
            cookies = cache.get('BIGPONDCOOKIES')
            session.cookies.update(json.loads(cookies))
            session.headers = config.APIGEE_HEADERS
            session.headers.update({'ovs-token': token.get('tokenId'),
                                    'ovs-uuid': token.get('uuid')})
    return token