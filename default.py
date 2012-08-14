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

from plugin import plugin


@plugin.route('/')
def view_top():
  addDirectoryItem(plugin.handle, plugin.url_for("/live"), ListItem("Direkte"), True)
  addDirectoryItem(plugin.handle, plugin.url_for("/recommended"), ListItem("Aktuelt"), True)
  addDirectoryItem(plugin.handle, plugin.url_for("/mostrecent"), ListItem("Siste"), True)
  addDirectoryItem(plugin.handle, plugin.url_for("/categories"), ListItem("Kategorier"), True)
  addDirectoryItem(plugin.handle, plugin.url_for("/letters"), ListItem("A-Å"), True)
  endOfDirectory(plugin.handle)

@plugin.route('/live')
def live():
  img_path = os.path.join(ADDON_PATH, "resources/images")
  add_item("NRK 1", "http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master_Layer%s.m3u8" % BITRATE, os.path.join(img_path, "nrk1.png"))
  add_item("NRK 2", "http://nrk2-i.akamaihd.net/hls/live/201544/nrk2/master_Layer%s.m3u8" % BITRATE, os.path.join(img_path, "nrk2.png"))
  add_item("NRK 3", "http://nrk3-i.akamaihd.net/hls/live/201545/nrk3/master_Layer%s.m3u8" % BITRATE, os.path.join(img_path, "nrk3.png"))
  
  olbitrate = BITRATE + 1
  add_item("OL 1", "http://hlswebvid23-i.akamaihd.net/hls/live/204296/hlswebvid23/master_Layer%s.m3u8" % olbitrate)
  add_item("OL 2", "http://hlswebvid24-i.akamaihd.net/hls/live/204297/hlswebvid24/master_Layer%s.m3u8" % olbitrate)
  add_item("OL 3", "http://hlswebvid25-i.akamaihd.net/hls/live/204298/hlswebvid25/master_Layer%s.m3u8" % olbitrate)
  add_item("OL 4", "http://hlswebvid26-i.akamaihd.net/hls/live/203761/hlswebvid26/master_Layer%s.m3u8" % olbitrate)
  add_item("OL 5", "http://hlswebvid27-i.akamaihd.net/hls/live/203543/hlswebvid27/master_Layer%s.m3u8" % olbitrate)
  add_item("OL 6", "http://hlswebvid28-i.akamaihd.net/hls/live/203544/hlswebvid28/master_Layer%s.m3u8" % olbitrate)
  add_item("OL 7", "http://hlswebvid29-i.akamaihd.net/hls/live/203545/hlswebvid29/master_Layer%s.m3u8" % olbitrate)
  endOfDirectory(plugin.handle)

def add_item(title, url, thumb=""):
  li =  ListItem(title, thumbnailImage=thumb)
  li.setProperty('mimetype', 'application/x-mpegURL')
  addDirectoryItem(plugin.handle, url, li, False)


def view(titles, urls, descr=repeat(''), thumbs=repeat(''), bgs=repeat('')):
  total = len(titles)
  for title, url, descr, thumb, bg in zip(titles, urls, descr, thumbs, bgs):
    descr = descr() if callable(descr) else descr
    thumb = thumb() if callable(thumb) else thumb
    bg = bg() if callable(bg) else bg
    li = ListItem(title, thumbnailImage=thumb)
    playable = plugin.route_for(url) == play
    li.setProperty('isplayable', str(playable))
    li.setProperty('fanart_image', bg)
    if playable:
      li.setInfo('video', {'plot':descr})
    addDirectoryItem(plugin.handle, plugin.url_for(url), li, not playable, total)
  endOfDirectory(plugin.handle)


@plugin.route('/recommended')
def recommended():
  titles, urls, bgs = data.parse_recommended()
  view(titles, urls, bgs=bgs)

@plugin.route('/mostrecent')
def mostrecent():
  titles, urls, thumbs = data.parse_most_recent()
  view(titles, urls, thumbs=thumbs)

@plugin.route('/categories')
def categories():
  titles, urls = data.parse_categories()
  view(titles, urls)

@plugin.route('/kategori/<arg>')
def category(arg):
  titles, urls = data.parse_by_category(arg)
  view(titles, urls)

@plugin.route('/letters')
def letters():
  common = ['0-9'] + map(chr, range(97, 123))
  titles = common + [ u'æ', u'ø', u'å' ]
  titles = [ e.upper() for e in titles ]
  urls = [ '/letters/%s' % l for l in (common + ['ae', 'oe', 'aa']) ]
  view(titles, urls)

@plugin.route('/letters/<arg>')
def letter(arg):
  titles, urls = data.parse_by_letter(arg)
  view(titles, urls)

@plugin.route('/serie/<arg>')
def seasons(arg):
  titles, urls = data.parse_seasons(arg)
  if len(titles) == 1:
    plugin.redirect(plugin.url_for(urls[0]))
    return
  view(titles, urls)

@plugin.route('/program/Episodes/<series_id>/<season_id>')
def episodes(series_id, season_id):
  titles, urls, descr = data.parse_episodes(series_id, season_id)
  view(titles, urls, descr=descr)

@plugin.route('/serie/<series_id>/<video_id>/.*')
@plugin.route('/program/<video_id>')
@plugin.route('/program/<video_id>/.*')
def play(video_id, series_id=""):
  url = data.parse_media_url(video_id, BITRATE)
  xbmcplugin.setResolvedUrl(plugin.handle, True, ListItem(path=url))
  player = xbmc.Player()
  subtitle = subs.get_subtitles(video_id)
  #Wait for stream to start
  start_time = time.time()
  while not player.isPlaying() and time.time() - start_time < 10:
    time.sleep(1.)
    player.setSubtitles(subtitle)
    if not SHOW_SUBS:
      player.showSubtitles(False)

if ( __name__ == "__main__" ):
  plugin.run()

