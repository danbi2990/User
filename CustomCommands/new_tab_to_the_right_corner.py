# import sublime
import sublime_plugin


def move_tab_to_the_end(view):
    window = view.window()
    (group, current) = window.get_view_index(view)
    last_index = len(window.views_in_group(group)) - 1
    window.set_view_index(view, group, last_index)


class NewTabToTheRightCornerListener(sublime_plugin.EventListener):

    def on_new(self, view):
        move_tab_to_the_end(view)
        # def callback(view=view):
        #     return self._move_tab_to_the_end(view)

        # sublime.set_timeout(callback, 100)

    # def on_load(self, view):

    #     move_tab_to_the_end(view)
        # window = sublime.active_window()

    # def __init__(self):
    #     self.previous_view_index = None

    # def _move_tab_to_the_end(self, view):
    #     window = sublime.active_window()
    #     (group, current) = window.get_view_index(view)
    #     last_index = len(window.views_in_group(group)) - 1
    #     window.set_view_index(view, group, last_index)

        # transient = window.transient_view_in_group(group)
        # print(transient)

        # views = window.views()
        # for view in views:
        #     print(view.id(), end=', ')

        # print()
        # views2 = window.views_in_group(group)
        # for view in views2:
        #     print(view.id(), end=', ')
        # if current != last_index:
        #     self.previous_view_index = current - 1

        # transient = sublime_api.window_transient_view_in_group(window.id(), group)
        # print(transient)
        # for view in window.views():
        #     file = view.file_name()
        #     print(file)
        # result = window.find_open_file(file)

        # sublime.set_timeout(window.set_view_index(view, group, last_index), 100)

    # def on_activated(self, view):
    #     pass

    # def on_close(self, view):
    #     window = sublime.active_window()
    #     window.focus_view(self.previous_view)

        # is_preview = view.file_name() is not "None" \
        #     and window \
        #     and view.file_name() not in \
        #     [file.file_name() for file in window.views()]

        # print(is_preview)
