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
from xbmcgui import ListItem
from BeautifulSoup import BeautifulSoup
import re, htmlentitydefs

parseDOM = common.parseDOM

html_decode = lambda string: BeautifulSoup(string,
    convertEntities=BeautifulSoup.HTML_ENTITIES).contents[0]

##
# Removes HTML or XML character references and entities from a text string.
# from: http://effbot.org/zone/re-sub.htm#unescape-html
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.

def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

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
  
  titles1 = parseDOM(html, 'strong')
  titles2 = parseDOM(html, 'a')
  titles = [ "%s - %s" % (t1, t2) for t1, t2 in zip(titles1, titles2) ]
  #titles = map(html_decode, titles)
  
  urls = parseDOM(html, 'a', ret='href')
  imgs = re.findall(r'1900":"([^"]+)', html)
  return titles, urls, imgs


def parse_most_recent():
  url = "http://tv.nrk.no/listobjects/recentlysent"
  html = urllib2.urlopen(url).read()
  urls = parseDOM(html, 'a', {'class':'listobject-link'}, ret='href')
  urls = [ e.split('http://tv.nrk.no/')[1] for e in urls ]
  thumbs = parseDOM(html, 'img', ret='src')
  dates = parseDOM(html, 'time')
  titles = parseDOM(html, 'img', ret='alt')
  titles = [ "%s %s" % (t,d) for t,d in zip(titles, dates) ]
  titles = map(html_decode, titles)
  return titles, urls, thumbs


def parse_seasons(arg):
  """ in: </serie/aktuelt-tv> """
  """ out: </program/Episodes/aktuelt-tv/11998> """
  url = "http://tv.nrk.no/%s" % arg
  html = urllib2.urlopen(url).read()
  html = parseDOM(html, 'div', {'id':'seasons'})
  html = parseDOM(html, 'noscript')
  titles = parseDOM(html, 'a', {'id':'seasonLink-.*?'})
  titles = [ "Sesong %s" % html_decode(t) for t in titles ]
  ids = parseDOM(html, 'a', {'id':'seasonLink-.*?'}, ret='href')
  return titles, ids


def parse_episodes(arg):
  """ in: </program/Episodes/aktuelt-tv/11998> """
  """ out: </serie/aktuelt-tv/nnfa50051612/16-05-2012> """
  url = "http://tv.nrk.no/%s" % arg
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
  info = {}
  #title = parseDOM(html, 'meta', {'name':'seriestitle'}, ret='content')[0]
  url = parseDOM(html, 'div', {'id':'player'}, ret='\tdata-media')[0]
  url = url.replace('/z/', '/i/', 1)
  url = url.rsplit('/', 1)[0]
  url = url + '/index_%s_av.m3u8' % bitrate
  title = re.findall('<h1>(.*?)</h1>',html,re.DOTALL)[0].strip()
  title = title.replace('<span class="small">',"").replace('</span>',"").replace("\n","").replace("\t","")
  title = unescape(title)
  li = ListItem(label=title,path=url)
  try:
    img = parseDOM(html, 'meta', {'name':'og:image'}, ret='content')[0]
    li.setIconImage(img)
    li.setThumbnailImage(img)
  except IndexError:
    print 'No imgage'
  info = {'title':title}
  try:
    info['plot'] = parseDOM(html, 'meta', {'name':'og:description'}, ret='content')[0]
  except IndexError:
    pass
  
  li.setInfo('video',info)
  subtitle = None
  try:
    subtitle = 'http://tv.nrk.no%s' % re.findall('data-subtitlesurl = "(.*?)"',html)[0]
  except IndexError:
    pass
  return li, subtitle


