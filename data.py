'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import re
import urllib2
import CommonFunctions as common
from BeautifulSoup import BeautifulSoup

parseDOM = common.parseDOM

html_decode = lambda string: BeautifulSoup(string,
    convertEntities=BeautifulSoup.HTML_ENTITIES).contents[0]


def parse_by_letter(arg):
  """ in: <n> """
  """ out: </serie/newton> or </program/koif45000708> """
  url = "http://tv.nrk.no/programmer/%s?filter=rettigheter" % arg
  html = urllib2.urlopen(url).read()
  html = parseDOM(html, 'div', {'id':'programList'})
  titles = parseDOM(html, 'a', {'class':''})
  titles = map(html_decode, titles)
  urls = parseDOM(html, 'a', {'class':''}, ret='href')
  return titles, urls


def parse_recommended():
  url = "http://tv.nrk.no/"
  html = urllib2.urlopen(url).read()
  html = parseDOM(html, 'ul', {'id':'introSlider'})[0]
  
  titles1 = parseDOM(html, 'a')
  titles2 = parseDOM(html, 'strong')
  titles = [ "%s - %s" % (t1, t2) for t1, t2 in zip(titles1, titles2) ]
  titles = map(html_decode, titles)
  
  urls = parseDOM(html, 'a', ret='href')
  imgs = re.findall(r'1900":"([^"]+)', html)
  return titles, urls, imgs


def parse_most_recent():
  url = "http://tv.nrk.no/listobjects/recentlysent"
  html = urllib2.urlopen(url).read()
  urls = parseDOM(html, 'a', {'class':'listobject-link'}, ret='href')
  urls = [ e.split('http://tv.nrk.no/')[1] for e in urls ]
  thumbs = parseDOM(html, 'img', ret='data-src')
  dates = parseDOM(html, 'time')
  titles = parseDOM(html, 'img', ret='alt')
  titles = [ "%s %s" % (t,d) for t,d in zip(titles, dates) ]
  titles = map(html_decode, titles)
  return titles, urls, thumbs


def parse_seasons(arg):
  """ in: </serie/nytt-paa-nytt> """
  """ out: <nytt-paa-nytt 8246> """
  url = "http://tv.nrk.no/%s" % arg
  html = urllib2.urlopen(url).read()
  html = parseDOM(html, 'div', {'id':'oldSeasons'})
  titles = parseDOM(html, 'a', {'id':'seasonLink-.*?'})
  titles = map(html_decode, titles)
  season_ids = parseDOM(html, 'a', {'id':'seasonLink-.*?'}, ret='id')
  season_ids = [ e.split('-')[-1] for e in season_ids ]
  
  series_id = url.split('/')[-1]
  args = [ '%s %s' % (series_id, season) for season in season_ids ]
  return titles, args


def parse_episodes(arg):
  """ in: <nytt-paa-nytt 8246> """
  """ out: <serie/nytt-paa-nytt/muhh40001512> """
  series_id, season_id = arg.split()
  url = "http://tv.nrk.no/program/Episodes/%s/%s" % (series_id, season_id)
  
  html = urllib2.urlopen(url).read()
  html = parseDOM(html, 'table', {'class':'episodeTable'})
  trs = parseDOM(html, 'tr', {'class':'has-programtooltip episode-row js-click *'})
  titles = [ parseDOM(tr, 'a', {'class':'p-link'})[0] for tr in trs ]
  titles = map(html_decode, titles)
  urls = [ parseDOM(tr, 'a', {'class':'p-link'}, ret='href')[0] for tr in trs ]
  ids = [ e.split('http://tv.nrk.no/')[1] for e in urls ]
  return titles, ids


def parse_media_url(arg, bitrate=4):
  url = "http://tv.nrk.no/%s" % arg
  html = urllib2.urlopen(url).read()
  #title = parseDOM(html, 'meta', {'name':'seriestitle'}, ret='content')[0]
  url = parseDOM(html, 'div', {'id':'player'}, ret='data-media')[0]
  url = url.replace('/z/', '/i/', 1)
  url = url.rsplit('/', 1)[0]
  url = url + '/index_%s_av.m3u8' % bitrate
  return url


