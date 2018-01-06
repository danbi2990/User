# import sublime
import sublime_plugin


def is_revealed(window):
    window.run_command("reveal_in_side_bar")
    return window.is_sidebar_visible()


class ToggleAndFocusSidebar(sublime_plugin.WindowCommand):

    def __init__(self, window):
        super().__init__(window)
        self.previous_group = 0

    def run(self):
        visible = self.window.is_sidebar_visible()
        if visible:
            self.window.focus_group(self.previous_group)
            self.window.run_command("toggle_side_bar")
        else:
            self.previous_group = self.window.active_group()
            is_revealed(self.window) \
                or self.window.run_command("toggle_side_bar")
            self.window.run_command("focus_side_bar")


class RevealAndFocusSidebar(sublime_plugin.WindowCommand):

    def __init__(self, window):
        super().__init__(window)

    def run(self):
        self.window.run_command("reveal_in_side_bar")
        self.window.run_command("focus_side_bar")
