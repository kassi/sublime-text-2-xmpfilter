import os, sublime, sublime_plugin, subprocess

class ExecuteAndUpdateRubyMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        text = self.view.substr(region)
        shell = os.name == "nt"

        s = subprocess.Popen(
            [ '/usr/bin/env', 'xmpfilter' ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=shell,
            universal_newlines=True )
        output, error = s.communicate(text)

        if s.returncode != None and s.returncode != 0:
            sublime.message_dialog("There was an error: " + error)
            return

        self.view.replace(edit, region, output)

class SetRubyMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        text = self.view.substr(region)

        s = subprocess.Popen(
            [ '/usr/bin/env', 'xmpfilter', '-m' ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=shell,
            universal_newlines=True )
        output, error = s.communicate(text)

        if s.returncode != None and s.returncode != 0:
            sublime.message_dialog("There was an error: " + error)
            return

        self.view.replace(edit, region, output)
