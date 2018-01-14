# Copyright 2016 Glenn Guy
# This file is part of NRL Live Kodi Addon
#
# NRL Live is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NRL Live is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NRL Live.  If not, see <http://www.gnu.org/licenses/>.

import urlparse
import unicodedata
import urllib


class movie():
    """
    movie/tv show info container
    """
    def __init__(self):
        self.video_id = None
        self.qual = None
        self.thumb = None
        self.fanart = None
        self.title = None
        self.shortdesc = None
        self.longdesc = None
        self.genre = None
        self.director = None
        self.cast = None
        self.duration = None
        self.year = None
        self.dummy = None

    def make_kodi_url(self):
        d = self.__dict__
        for key, value in d.iteritems():
            if isinstance(value, unicode):
                d[key] = unicodedata.normalize(
                    'NFKD', value).encode('ascii', 'ignore')
        url = ''
        if d['thumb']:
            d['thumb'] = urllib.quote_plus(d['thumb'])
        if d['fanart']:
            d['fanart'] = urllib.quote_plus(d['fanart'])
        for item in d.keys():
            url += '&{0}={1}'.format(item, d[item])
        return url

    def parse_kodi_url(self, url):
        params = urlparse.parse_qsl(url)
        for item in params.keys():
            setattr(self, item, urllib.unquote_plus(params[item]))

    def get_art(self):
        d = {}
        if self.fanart:
            d['fanart'] = urllib.unquote_plus(self.fanart)
        return d

    def get_info(self):
        d = {}
        if self.genre:
            d['genre'] = self.genre[0]
        if self.shortdesc:
            d['plotoutline'] = self.shortdesc
        if self.longdesc:
            d['plot'] = self.longdesc
        if self.director:
            d['director'] = ', '.join(x for x in self.director)
        if self.cast:
            d['cast'] = [x['name'] for x in self.cast]
        if self.year:
            d['year'] = self.year
        return d

    def get_stream_info(self):
        d = {}
        d['codec'] = 'h264'
        if self.duration:
            d['duration'] = self.duration
        if self.qual == 'HD':
            d['width'] = 1280
            d['height'] = 720
        else:
            d['width'] = 960
            d['height'] = 540
        return d
