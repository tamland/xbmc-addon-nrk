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
from datetime import datetime, timedelta
from data import parse_media_url
import xbmc
import os

parseDOM = common.parseDOM


def getSubtitles(path):
    url = 'http://tv.nrk.no/%s' % path
    html = urllib2.urlopen(url).read()
    url = 'http://tv.nrk.no%s' % re.findall('data-subtitlesurl = "(.*?)"',html)[0]
    xbmc.log('NRK:'+url)
    title =  re.findall('og:title" content="(.*?)"',html)[0]
    episodenr = re.findall('episodenumber" content="(.*?)"',html)
    if episodenr:
        title += ' '+episodenr
    filename = os.path.join(xbmc.translatePath("special://temp"), title+'.no.srt') 
    f = open(filename, 'w')
    html = urllib2.urlopen(url).read()
    parts  = parseDOM(html, 'p',ret={'begin'})
    i = 0
    for p in parts:
        i += 1
        f.write(str(i))
        begint = parseDOM(p,'p',ret='begin')
        dur = parseDOM(p,'p',ret='dur')
        begin = datetime.strptime(begint[0],'%H:%M:%S.%f')
        dur = datetime.strptime(dur[0],'%H:%M:%S.%f')
        dur = timedelta(0,dur.hour*3600+dur.minute*60+dur.second,dur.microsecond)
        end = begin+dur
        f.write('\n%02d:%02d:%02d,%03d' % (begin.hour,begin.minute,begin.second,begin.microsecond/1000))
        f.write(' --> %02d:%02d:%02d,%03d\n' % (end.hour,end.minute,end.second,end.microsecond/1000))
        f.write(re.sub('<br></br>\s*','\n',' '.join(parseDOM(p,'p')[0].replace('<span style="italic">','<i>').replace('</span>','</i>').split())))
        f.write('\n\n')

    return filename

print getSubtitles('serie/funny-or-die-presents/koif60002110/sesong-1/episode-1')
