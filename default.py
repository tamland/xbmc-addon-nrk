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

import os
import sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import data
import CommonFunctions as common

from itertools import repeat
from xbmcplugin import addDirectoryItem
from xbmcplugin import endOfDirectory
from xbmcgui import ListItem

ADDON = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')


def view_top(handle, base_url):
  addDirectoryItem(handle, base_url+"?node=live", ListItem("Direkte"), True)
  addDirectoryItem(handle, base_url+"?node=recommended", ListItem("Aktuelt"), True)
  addDirectoryItem(handle, base_url+"?node=mostrecent", ListItem("Siste"), True)
  addDirectoryItem(handle, base_url+"?node=letters", ListItem("A-Å"), True)
  endOfDirectory(handle)

def view_live(handle, base_url):
  bitrate = 3
  img_path = os.path.join(ADDON_PATH, "resources/images")
  addDirectoryItem(handle,
      "http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master_Layer%s.m3u8" % bitrate,
      ListItem("NRK 1", thumbnailImage=os.path.join(img_path, "nrk1.png")), False)
  addDirectoryItem(handle,
      "http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master_Layer%s.m3u8" % bitrate,
      ListItem("NRK 2", thumbnailImage=os.path.join(img_path, "nrk2.png")), False)
  addDirectoryItem(handle,
      "http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master_Layer%s.m3u8" % bitrate,
      ListItem("NRK 3", thumbnailImage=os.path.join(img_path, "nrk3.png")), False)
  endOfDirectory(handle)

def view_dir(handle, base_url, nodes, args, titles, thumbs=repeat(''), bgs=repeat('')):
  total = len(titles)
  for node, arg, title, thumb, bg in zip(nodes, args, titles, thumbs, bgs):
    thumb = thumb() if callable(thumb) else thumb
    bg = bg() if callable(bg) else bg
    li = ListItem(title, thumbnailImage=thumb)
    url = "%s?node=%s&arg=%s" % (base_url, node, arg)
    isdir = node != 'play'
    li.setProperty('isplayable', str(not isdir))
    li.setProperty('fanart_image', bg)
    addDirectoryItem(handle, url, li, isdir, total)
  endOfDirectory(handle)


def controller(handle, base_url, node, arg):
  if node == 'live':
    view_live(handle, base_url)
  
  elif node == 'recommended':
    titles, args, imgs = data.parse_recommended()
    view_dir(handle, base_url, repeat('play'), args, titles, imgs, imgs)
  
  elif node == 'mostrecent':
    titles, args, thumbs = data.parse_most_recent()
    view_dir(handle, base_url, repeat('play'), args, titles, thumbs)
  
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
  
  elif node == 'seasons':
    titles, args = data.parse_seasons(arg)
    nodes = repeat('episodes')
    if len(titles) == 1:
      titles, args = data.parse_episodes(args[0])
      nodes = repeat('play')
    view_dir(handle, base_url, nodes, args, titles)
  
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

