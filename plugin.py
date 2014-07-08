#!/usr/bin/env python
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
import re
import sys
import xbmc, xbmcaddon
import cgi

class Plugin(object):
  def __init__(self):
    self._routes = []
    self._addon = xbmcaddon.Addon()
    self.handle = int(sys.argv[1])
    self.args = sys.argv[2][1:]
    self.addon_id = self._addon.getAddonInfo('id')
    self.path = self._addon.getAddonInfo('path')
  
  def get_setting(self, key):
    return self._addon.getSetting(id=key)
  
  def make_url(self, url):
    return 'plugin://%s%s' % (self.addon_id, url)
  
  def route_for(self, path):
    for rule in self._routes:
      view_func, items = rule.match(path)
      if view_func:
        return view_func
    return None
  
  def route(self, url_rule):
    def decorator(f):
      rule = UrlRule(url_rule, f)
      self._routes.append(rule)
      return f
    return decorator
  
  def run(self):
    if self.args:
      queries = cgi.parse_qs(self.args)
      q = {}
      for key, value in queries.items():
        q[key] = value[0]
      self._dispatch(q[key])
    path = sys.argv[0].split('plugin://%s' % self.addon_id)[1] or '/'
    self._dispatch(path)
  
  def redirect(self, path):
    self._dispatch(path)
  
  def _dispatch(self, path):
    for rule in self._routes:
      view_func, kwargs = rule.match(path)
      if view_func:
        view_func(**kwargs)
        return

class UrlRule(object):
  def __init__(self, url_rule, view_func):
    self._view_func = view_func
    p = re.sub('<([A-z]*)>', '<string:\\1>', url_rule)
    
    p = re.sub('<string:([A-z]+)>', '(?P<\\1>[^/]+?)', p)
    p = re.sub('<path:([A-z]+)>', '(?P<\\1>.*)', p)
    self._regex = re.compile('^' + p + '$')
  
  def match(self, path):
    m = self._regex.search(path)
    if not m:
      return False, None
    return self._view_func, m.groupdict()
