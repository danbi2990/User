# import sublime
import sublime_plugin


class ToggleMenubar(sublime_plugin.WindowCommand):

    def run(self):
        w = self.window
        w.set_menu_visible(not w.is_menu_visible())
