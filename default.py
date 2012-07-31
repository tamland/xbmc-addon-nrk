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
import time
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import data
import subs
import CommonFunctions as common

from itertools import repeat
from xbmcplugin import addDirectoryItem
from xbmcplugin import endOfDirectory
from xbmcgui import ListItem

ADDON = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')
BITRATE = int(ADDON.getSetting('bitrate')) + 1
SHOW_SUBS = ADDON.getSetting('showsubtitles')


def view_top(handle, base_url):
  addDirectoryItem(handle, base_url+"?node=live", ListItem("Direkte"), True)
  addDirectoryItem(handle, base_url+"?node=recommended", ListItem("Aktuelt"), True)
  addDirectoryItem(handle, base_url+"?node=mostrecent", ListItem("Siste"), True)
  addDirectoryItem(handle, base_url+"?node=letters", ListItem("A-Å"), True)
  endOfDirectory(handle)

def view_live(handle, base_url):
  img_path = os.path.join(ADDON_PATH, "resources/images")
  add_item(handle, "NRK 1", "http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master_Layer%s.m3u8" % BITRATE, os.path.join(img_path, "nrk1.png"))
  add_item(handle, "NRK 2", "http://nrk2-i.akamaihd.net/hls/live/201544/nrk2/master_Layer%s.m3u8" % BITRATE, os.path.join(img_path, "nrk2.png"))
  add_item(handle, "NRK 3", "http://nrk3-i.akamaihd.net/hls/live/201545/nrk3/master_Layer%s.m3u8" % BITRATE, os.path.join(img_path, "nrk3.png"))
  
  olbitrate = BITRATE + 1
  add_item(handle, "OL 1", "http://hlswebvid23-i.akamaihd.net/hls/live/204296/hlswebvid23/master_Layer%s.m3u8" % olbitrate)
  add_item(handle, "OL 2", "http://hlswebvid24-i.akamaihd.net/hls/live/204297/hlswebvid24/master_Layer%s.m3u8" % olbitrate)
  add_item(handle, "OL 3", "http://hlswebvid25-i.akamaihd.net/hls/live/204298/hlswebvid25/master_Layer%s.m3u8" % olbitrate)
  add_item(handle, "OL 4", "http://hlswebvid26-i.akamaihd.net/hls/live/203761/hlswebvid26/master_Layer%s.m3u8" % olbitrate)
  add_item(handle, "OL 5", "http://hlswebvid27-i.akamaihd.net/hls/live/203543/hlswebvid27/master_Layer%s.m3u8" % olbitrate)
  add_item(handle, "OL 6", "http://hlswebvid28-i.akamaihd.net/hls/live/203544/hlswebvid28/master_Layer%s.m3u8" % olbitrate)
  add_item(handle, "OL 7", "http://hlswebvid29-i.akamaihd.net/hls/live/203545/hlswebvid29/master_Layer%s.m3u8" % olbitrate)
  endOfDirectory(handle)

def add_item(handle, title, url, thumb=""):
  li =  ListItem(title, thumbnailImage=thumb)
  li.setProperty('mimetype', 'application/x-mpegURL')
  addDirectoryItem(handle, url, li, False)


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
    titles, args, bgs = data.parse_recommended()
    view_dir(handle, base_url, repeat('play'), args, titles, bgs=bgs)
  
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
    url, subtitle_url = data.parse_media_url(arg, BITRATE)
    xbmcplugin.setResolvedUrl(handle, True, ListItem(path=url))
    if subtitle_url:
      player = xbmc.Player()
      subtitle = subs.get_subtitles(subtitle_url)
      # Waiting for stream to start
      start_time = time.time()
      while not player.isPlaying() and time.time() - start_time < 10:
        time.sleep(1.)
      player.setSubtitles(subtitle)
      if not SHOW_SUBS:
        player.showSubtitles(False)
  
  else:
    view_top(handle, base_url)

if ( __name__ == "__main__" ):
  base_url = sys.argv[0]
  handle   = int(sys.argv[1])
  params   = common.getParameters(sys.argv[2])
  
  node = params['node'] if 'node' in params else ""
  arg = params['arg'] if 'arg' in params else ""
  controller(handle, base_url, node, arg)

