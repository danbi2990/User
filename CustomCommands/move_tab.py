# import sublime
import sublime_plugin


class MoveTab(sublime_plugin.WindowCommand):

    def run(self, offset):
        view = self.window.active_view()
        (group, current) = self.window.get_view_index(view)

        end = len(self.window.views_in_group(group))
        destination = current + int(offset)
        if destination < 0 or destination == end:
            return

        self.window.set_view_index(view, group, destination)
        # self.window.focus_view(view)

    def is_enabled(self):
        view = self.window.active_view()
        if view is None:
            return False
        (group, index) = self.window.get_view_index(view)
        return len(self.window.views_in_group(group)) > 1

    def is_visible(self):
        return True

    def description(self):
        return None
