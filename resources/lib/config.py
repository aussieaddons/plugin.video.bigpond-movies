# flake8: noqa
import version

NAME = 'Bigpond Movies'
ADDON_ID = 'plugin.video.bigpond-movies'
VERSION = version.VERSION

GITHUB_API_URL = 'https://api.github.com/repos/glennguy/plugin.video.bigpond-movies'
ISSUE_API_URL = GITHUB_API_URL + '/issues'
ISSUE_API_AUTH = 'eGJtY2JvdDo1OTQxNTJjMTBhZGFiNGRlN2M0YWZkZDYwZGQ5NDFkNWY4YmIzOGFj'
GIST_API_URL = 'https://api.github.com/gists'

MAX_LIVEQUAL = 4
MAX_REPLAYQUAL = 7


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
