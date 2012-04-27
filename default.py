# -*- coding: utf-8 -*-
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

import sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import data
import CommonFunctions as common

from itertools import repeat
from xbmcplugin import addDirectoryItem
from xbmcplugin import endOfDirectory
from xbmcgui import ListItem

addon = xbmcaddon.Addon(id="plugin.video.nrk")
#data.setQuality(int(addon.getSetting("quality")))


def view_top(handle, base_url):
  addDirectoryItem(handle, base_url+"?node=live",     ListItem("Direkte"), True)
  addDirectoryItem(handle, base_url+"?node=letters",  ListItem("A-Å"), True)
  #addDirectoryItem(handle, base_url+"?node=genres",   ListItem(""), True)
  #addDirectoryItem(handle, base_url+"?node=latest",   xbmcgui.ListItem(_(30102)), True)
  #addDirectoryItem(handle, base_url+"?node=topweek",  xbmcgui.ListItem(_(30106)), True)
  #addDirectoryItem(handle, base_url+"?node=topmonth", xbmcgui.ListItem(_(30107)), True)
  #addDirectoryItem(handle, base_url+"?node=toptotal", xbmcgui.ListItem(_(30108)), True)
  #addDirectoryItem(handle, base_url+"?node=search",   xbmcgui.ListItem(_(30105)), True)
  endOfDirectory(handle)

def view_live(handle, base_url):
  bitrate = 3
  addDirectoryItem(handle, "http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master_Layer%s.m3u8" % bitrate, ListItem("NRK 1"), False)
  addDirectoryItem(handle, "http://nrk2-i.akamaihd.net/hls/live/201544/nrk2/master_Layer%s.m3u8" % bitrate, ListItem("NRK 2"), False)
  addDirectoryItem(handle, "http://nrk3-i.akamaihd.net/hls/live/201545/nrk3/master_Layer%s.m3u8" % bitrate, ListItem("NRK 3"), False)
  endOfDirectory(handle)

def view_dir(handle, base_url, nodes, args, titles):
  items = []
  for node, arg, title in zip(nodes, args, titles):
    li = ListItem(title, thumbnailImage="")
    li.setInfo( type="Video", infoLabels={"title": title, "plot":"e.description", "tvshowtitle":"e.title"} )
    url = "%s?node=%s&arg=%s" % (base_url, node, arg)
    isdir = node != 'play'
    li.setProperty('IsPlayable',str(not isdir))
    items.append((url, li, isdir))
  xbmcplugin.addDirectoryItems(handle=handle, items=items)
  xbmcplugin.endOfDirectory(handle)

def node_search(baseUrl, handle):
    kb = xbmc.Keyboard()
    kb.doModal()
    if (kb.isConfirmed()):
        text = kb.getText()
        dataItems = Data.getSearchResults(text)
        create(baseUrl, handle, dataItems)
    

def controller(handle, base_url, node, arg):
  if node == 'live':
    view_live(handle, base_url)
  
  elif node == 'letters':
    common = ['0-9'] + map(chr, range(97, 123))
    titles = common + [ u'æ', u'ø', u'å' ]
    titles = [ e.upper() for e in titles ]
    args = common + [ 'ae', 'oe', 'aa' ]
    view_dir(handle, base_url, repeat('letter'), args, titles)
  
  elif node == 'letter':
    titles, args = data.parse_by_letter(arg)
    nodes = ( 'seasons' if arg.startswith('/serie') else 'play' for arg in args )
    view_dir(handle, base_url, nodes, args, titles)
  
  elif node == 'mostpopular':
    titles, args = data.parse_most_popular()
    view_dir(handle, base_url, repeat('play'), args, titles)
  
  elif node == 'seasons':
    titles, args = data.parse_seasons(arg)
    view_dir(handle, base_url, repeat('episodes'), args, titles)
  
  elif node == 'episodes':
    titles, args = data.parse_episodes(arg)
    view_dir(handle, base_url, repeat('play'), args, titles)
  
  elif node == 'play':
    url = data.parse_media_url(arg)
    xbmcplugin.setResolvedUrl(handle, True, ListItem(path=url))
  
  else:
    view_top(handle, base_url)

if ( __name__ == "__main__" ):
  base_url = sys.argv[0]
  handle   = int(sys.argv[1])
  params   = common.getParameters(sys.argv[2])

  node = params['node'] if 'node' in params else ""
  arg = params['arg'] if 'arg' in params else ""
  controller(handle, base_url, node, arg)

