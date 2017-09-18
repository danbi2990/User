import os
import sublime
import sublime_plugin


def copy_path(path):
    sublime.set_clipboard(path)


class CopyProjectFolderPath(sublime_plugin.WindowCommand):

    def run(self):
        if len(self.window.folders()) == 0:
            return

        copy_path(self.window.folders()[0])


class CopyFilePath(sublime_plugin.WindowCommand):

    def run(self):
        if self.window.active_view() is None:
            return

        copy_path(self.window.active_view().file_name())
        # copy_path(os.path.dirname(self.window.active_view().file_name()))


class CopyFileFolderPath(sublime_plugin.WindowCommand):

    def run(self):
        if self.window.active_view() is None:
            return

        copy_path(os.path.dirname(self.window.active_view().file_name()))
