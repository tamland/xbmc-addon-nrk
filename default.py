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
import time
import xbmc, xbmcplugin
from itertools import repeat
from urllib import quote
from xbmcplugin import addDirectoryItem
from xbmcplugin import endOfDirectory
from xbmcgui import ListItem
import plugin
plugin = plugin.Plugin()

BITRATE = int(plugin.get_setting('bitrate')) + 1
SHOW_SUBS = int(plugin.get_setting('showsubtitles')) == 1

@plugin.route('/')
def view_top():
  addDirectoryItem(plugin.handle, plugin.make_url("/live"), ListItem("Direkte"), True)
  addDirectoryItem(plugin.handle, plugin.make_url("/recommended"), ListItem("Aktuelt"), True)
  addDirectoryItem(plugin.handle, plugin.make_url("/mostrecent"), ListItem("Siste"), True)
  addDirectoryItem(plugin.handle, plugin.make_url("/categories"), ListItem("Kategorier"), True)
  addDirectoryItem(plugin.handle, plugin.make_url("/letters"), ListItem("A-Å"), True)
  addDirectoryItem(plugin.handle, plugin.make_url("/search"), ListItem("Søk"), True)
  endOfDirectory(plugin.handle)

@plugin.route('/live')
def live():
  add("NRK 1", "http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master.m3u8", "application/vnd.apple.mpegurl", "nrk1.png")
  add("NRK 2", "http://nrk2-i.akamaihd.net/hls/live/201544/nrk2/master.m3u8", "application/vnd.apple.mpegurl", "nrk2.png")
  add("NRK 3", "http://nrk3-i.akamaihd.net/hls/live/201545/nrk3/master.m3u8", "application/vnd.apple.mpegurl", "nrk3.png")
  add("NRK P1", "http://lyd.nrk.no/nrk_radio_p1_ostlandssendingen_mp3_h", "audio/mpeg")
  add("NRK P2", "http://lyd.nrk.no/nrk_radio_p2_mp3_h", "audio/mpeg")
  add("NRK P3", "http://lyd.nrk.no/nrk_radio_p3_mp3_h", "audio/mpeg")
  add("Alltid nyheter", "http://lyd.nrk.no/nrk_radio_alltid_nyheter_mp3_h", "audio/mpeg")
  add("Alltid RR", "http://lyd.nrk.no/nrk_radio_p3_radioresepsjonen_mp3_h", "audio/mpeg")
  add("Jazz", "http://lyd.nrk.no/nrk_radio_jazz_mp3_h", "audio/mpeg")
  add("Klassisk", "http://lyd.nrk.no/nrk_radio_klassisk_mp3_h", "audio/mpeg")
  add("Folkemusikk", "http://lyd.nrk.no/nrk_radio_folkemusikk_mp3_h", "audio/mpeg")
  add("Gull", "http://lyd.nrk.no/nrk_radio_gull_mp3_h", "audio/mpeg")
  add("mP3", "http://lyd.nrk.no/nrk_radio_mp3_mp3_h", "audio/mpeg")
  add("P3 Urørt", "http://lyd.nrk.no/nrk_radio_p3_urort_mp3_h", "audio/mpeg")
  add("Sport", "http://lyd.nrk.no/nrk_radio_sport_mp3_h", "audio/mpeg")
  add("Sápmi", "http://lyd.nrk.no/nrk_radio_sami_mp3_h", "audio/mpeg")
  add("Super", "http://lyd.nrk.no/nrk_radio_super_mp3_h", "audio/mpeg")
  endOfDirectory(plugin.handle)

def add(title, url, mimetype, thumb=""):
  if thumb:
    img_path = os.path.join(plugin.path, "resources/images")
    thumb = os.path.join(img_path, thumb)
  li =  ListItem(title, thumbnailImage=thumb)
  li.setProperty('mimetype', mimetype)
  addDirectoryItem(plugin.handle, url, li, False)

def view(titles, urls, thumbs=repeat(''), bgs=repeat(''), descr=repeat(''), update_listing=False):
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
      li.setInfo('video', {'title':title, 'plot':descr})
      li.addStreamInfo('video', {'codec':'h264', 'width':1280, 'height':720})
      li.addStreamInfo('audio', {'codec':'aac', 'channels':2})
      commands = []
      url = plugin.make_url( "/searchfor/%s" % title.encode('utf-8') )
      runner = "XBMC.ActivateWindow(Video," + url + ",return)"
      commands.append(( str("Search NRK..."), runner))
      li.addContextMenuItems( commands )
    addDirectoryItem(plugin.handle, plugin.make_url(url), li, not playable, total)
  endOfDirectory(plugin.handle, updateListing=update_listing)

@plugin.route('/recommended')
def recommended():
  import data
  view(*data.get_recommended())

@plugin.route('/mostrecent')
def mostrecent():
  import data
  view(*data.get_most_recent())

@plugin.route('/categories')
def categories():
  import data
  view(*data.get_categories())

@plugin.route('/kategori/<arg>')
def category(arg):
  import data
  view(*data.get_by_category(arg))

@plugin.route('/letters')
def letters():
  import data
  common = ['0-9'] + map(chr, range(97, 123))
  titles = common + [ u'æ', u'ø', u'å' ]
  titles = [ e.upper() for e in titles ]
  urls = [ '/letters/%s' % l for l in (common + ['ae', 'oe', 'aa']) ]
  view(titles, urls)

@plugin.route('/search')
def search():
  keyboard = xbmc.Keyboard(heading="Søk")
  keyboard.doModal()
  query = keyboard.getText()
  if query:
    plugin.redirect('/search/%s/1' % quote(query))

@plugin.route('/search/<query>/<page>')
def search_results(query, page):
  import data
  results = data.get_search_results(query, page)
  more_node = [ "Flere", '/search/%s/%s' % (query, int(page)+1), "", "" ]
  for i in range(0, len(more_node)):
    results[i].append(more_node[i])
  view(*results, update_listing=int(page) > 1)

@plugin.route('/searchfor/<query>')
def search_for(query):
  keyboard = xbmc.Keyboard(heading="Søk")
  keyboard.setDefault(query)
  keyboard.doModal()
  query = keyboard.getText()
  if query:
    plugin.redirect('/search/%s/1' % quote(query))

@plugin.route('/letters/<arg>')
def letter(arg):
  import data
  view(*data.get_by_letter(arg))

@plugin.route('/serie/<arg>')
def seasons(arg):
  import data
  titles, urls, thumbs, bgs = data.get_seasons(arg)
  if len(titles) == 1:
    return plugin.redirect(urls[0])
  view(titles, urls, thumbs=thumbs, bgs=bgs)

@plugin.route('/program/Episodes/<series_id>/<season_id>')
def episodes(series_id, season_id):
  import data
  view(*data.get_episodes(series_id, season_id))

@plugin.route('/serie/<series_id>/<video_id>/.*')
@plugin.route('/program/<video_id>')
@plugin.route('/program/<video_id>/.*')
def play(video_id, series_id=""):
  import data, subs
  url = data.get_media_url(video_id, BITRATE)
  xbmcplugin.setResolvedUrl(plugin.handle, True, ListItem(path=url))
  player = xbmc.Player()
  subtitle = subs.get_subtitles(video_id)
  if subtitle:
    #Wait for stream to start
    start_time = time.time()
    while not player.isPlaying() and time.time() - start_time < 10:
      time.sleep(1.)
    player.setSubtitles(subtitle)
    if not SHOW_SUBS:
      player.showSubtitles(False)

if  __name__ == '__main__':
  plugin.run()
