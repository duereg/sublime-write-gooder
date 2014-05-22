#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re
import os

SETTINGS_FILE = 'WriteGooder.sublime-settings'

class WriteGooderCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = sublime.load_settings(SETTINGS_FILE)
    cmd = settings.get('write-gooder', 'write-gooder')

    filepath = self.view.file_name()

    args = {
      "cmd": [
        cmd,
        filepath
      ],
      'line_regex': settings.get('line_regex', r"line (\d+) column (\d+): (.*)$"),
      'file_regex': settings.get('file_regex', r"write-gooder (.+)\]")
    }

    if sublime.platform() == "windows":
      args['cmd'][0] += ".cmd"
    elif sublime.platform() == "osx":
      args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin:/opt/boxen/nodenv/shims"

    self.view.window().run_command('exec', args)

class WriteGooderOnSave(sublime_plugin.EventListener):
  def on_post_save(self, view):
    settings = sublime.load_settings(SETTINGS_FILE)
    if settings.get('run_on_save', False) == False:
      return
    if re.search(settings.get('filename_filter'), view.file_name()):
      view.window().run_command("write_gooder")
      return