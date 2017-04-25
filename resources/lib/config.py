# flake8: noqa
import version

NAME = 'NRL Live'
ADDON_ID = 'plugin.video.nrl-live'
VERSION = version.VERSION

GITHUB_API_URL = 'https://api.github.com/repos/glennguy/plugin.video.nrl-live'
ISSUE_API_URL = GITHUB_API_URL + '/issues'
ISSUE_API_AUTH = 'eGJtY2JvdDo1OTQxNTJjMTBhZGFiNGRlN2M0YWZkZDYwZGQ5NDFkNWY4YmIzOGFj'
GIST_API_URL = 'https://api.github.com/gists'

MAX_LIVEQUAL = 4
MAX_REPLAYQUAL = 7



# url to send our Digital Pass info to
LOGIN_URL = ('https://signon-live-nrl.yinzcam.com/V1/Auth/Subscription?ff=mobile'
            '&mnc=1&app_version=3.3.0&carrier=&version=4.7'
            '&width=1080&height=1776&os_version=6.0&mcc=505'
            '&application=NRL_LIVE&os=Android')

# XML template to insert username and password into
LOGIN_DATA ='<Subscriber><Type>TDI</Type><User>{0}</User><Password>{1}</Password><Email>{0}</Email><AdobeCheckResult>0</AdobeCheckResult></Subscriber>'

# url used to request ooyala token
EMBED_TOKEN_URL = 'https://telstramedia-prod.apigee.net/v2/bpm/ovs/users/{0}/ooyalaToken?deviceType=android&embedCode={1}'

# url used to request playlist
AUTH_URL = ('http://player.ooyala.com/sas/player_api/v1/authorization/'
            'embed_code/{0}/{1}?device=generic&domain=http%3A%2F%2Fwww.ooyala.com&embedToken={2}'
            '&supportedFormats=dash%2Cm3u8%2Cmp4%2Chls')

QUERY_URL = 'https://telstramedia-prod.apigee.net/v2/bpm/screens/{0}?deviceType=android'

THANKS_URL = 'https://telstramedia-prod.apigee.net/v2/bpm/screens/thanks?deviceType=android'

FEATURED_URL = 'https://telstramedia-prod.apigee.net/v2/bpm/screens/featured?deviceType=android'

SERIES_URL = 'https://telstramedia-prod.apigee.net/v2/bpm/screens/purchases/assets/{0}?deviceType=android'


# ooyala provider indentifier code used in contructing request uris
PCODE = 'IzMmMyOqAXu_eSOyLuUx5jFPYMVU'

CATEGORIES = ['My Library',
              'Thanks Thursdays',
              'Featured',
              'Settings']

# New auth config for 2017

BIGPOND_URL = 'https://services.bigpond.com/rest/v1/AuthenticationService/authenticate?userIdentifierType=EMAIL&userIdentifier={0}&authToken={1}'

BIGPOND_HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Authorization': 'Basic bW92aWVzX2FuZHJvaWQ6cDlhajJWWGFqamp3QU5Odg==',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Pixel Build/N2G47E)',
                   'Accept-Encoding': 'gzip'}

APIGEE_URL = 'https://telstramedia-prod.apigee.net/v2/bpm/ovs/login?deviceType=android&realm=telstramedia&service=RaaToken&raaToken={0}&goto=https%3A%2F%2Ftelstramedia-prod.apigee.net%2Fv2%2Fbpm%2Fovs%2Fsessions'

APIGEE_HEADERS = {'Content-Type': 'application/json',
                  'user-agent': 'TSG',
                  'bpm-environment': 'bpm',
                  'Accept-Encoding': 'gzip'}



# WIDEVINE

SSD_WV_REPO = "https://github.com/glennguy/decryptmodules/raw/master/"
WIDEVINECDM_URL = { 'Linuxx86_64': 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb',
                    'Linuxarmv7': 'http://odroidxu.leeharris.me.uk/xu3/chromium-widevine-1.4.8.823-2-armv7h.pkg.tar.xz',
                    'Linuxarmv7': 'http://odroidxu.leeharris.me.uk/xu3/chromium-widevine-1.4.8.823-2-armv7h.pkg.tar.xz'}

UNARCHIVE_COMMAND = { 'Linuxx86_64': "(cd {1} && ar x {0} data.tar.xz && tar xJfO data.tar.xz ./opt/google/chrome/libwidevinecdm.so >{1}/{2} && chmod 755 {1}/{2} && rm -f data.tar.xz {0})",
                      'Linuxarmv7': "(cd {1} && tar xJfO {0} usr/lib/chromium/libwidevinecdm.so >{1}/{2} && chmod 755 {1}/{2} && rm -f {0})",
                      'Linuxarmv8': "(cd {1} && tar xJfO {0} usr/lib/chromium/libwidevinecdm.so >{1}/{2} && chmod 755 {1}/{2} && rm -f {0})"}
SSD_WV_DICT = { 'Windows': 'ssd_wv.dll',
                'Linux': 'libssd_wv.so',
                'Darwin': 'libssd_wv.dylib'}
WIDEVINECDM_DICT = { 'Windows': 'widevinecdm.dll',
                     'Linux': 'libwidevinecdm.so',
                     'Darwin': 'libwidevinecdm.dylib'}
SUPPORTED_PLATFORMS = [ 'WindowsAMD64',
                        'Windowsx86',
                        'Darwinx86_64',
                        'Linuxx86_64',
                        'Linuxarmv7',
                        'Linuxarmv8']

XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?><request protocol="3.0" 
version="chrome-55.0.2883.87" prodversion="55.0.2883.87" requestid="{{{0}}}" 
lang="en-US" updaterchannel="" prodchannel="" os="{1}" arch="{2}" 
nacl_arch="x86-64" wow64="1"><hw physmemory="12"/><os platform="Windows" 
arch="x86_64" version="10.0.0"/><app appid="oimompecagnajdejgnnjijobebaeigek" 
version="0.0.0.0" installsource="ondemand"><updatecheck/><ping rd="-2" 
ping_freshness=""/></app></request>"""

CRX_UPDATE_URL = "https://clients2.google.com/service/update2?cup2key=6:{0}&cup2hreq={1}"
