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
from data import parse_media_url
import xbmc
import os
import sys
import xbmcaddon

ADDON = xbmcaddon.Addon()
SUB_DELAY = float(ADDON.getSetting('subtitlesdelay'))


parseDOM = common.parseDOM

def getSubtitles(url):
    filename = os.path.join(xbmc.translatePath("special://temp"),'nrk.srt') 
    f = open(filename, 'w')
    html = urllib2.urlopen(url).read()
    parts  = parseDOM(html, 'p',ret={'begin'})
    i = 0
    for p in parts:
        begint = parseDOM(p,'p',ret='begin')[0]
        dur = parseDOM(p,'p',ret='dur')[0]
        begin = stringToTime(begint)
        dur = stringToTime(dur)
        end = begin+dur
        i += 1
        f.write(str(i))
        f.write('\n%s' % timeToString(begin))
        f.write(' --> %s\n' % timeToString(end))
        f.write(re.sub('<br></br>\s*','\n',' '.join(parseDOM(p,'p')[0].replace('<span style="italic">','<i>').replace('</span>','</i>').split())))
        f.write('\n\n')
    f.close()
    return filename

def stringToTime(txt):
    p = txt.split(':')
    return int(p[0])*3600+int(p[1])*60+float(p[2])

def timeToString(time):
    return '%02d:%02d:%02d,%03d' % (time/3600,(time%3600)/60,time%60,(time%1)*1000)
