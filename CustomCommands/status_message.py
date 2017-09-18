# import sublime
import re
import os
import sublime_plugin


def _set_status(view):
    # selections = view.sel()

    # if len(selections) != 1:
    #     message = '☰' + str(len(selections))
    # else:
    #     selection = selections[0]
    #     if selection.empty():
    #         row, col = view.rowcol(selections[0].b)
    #         message = 'λ' + str(row + 1) + ':' + str(col + 1)
    #     else:
    #         message = '#' + str(selection.size())

    message = ''
    # file_name = view.file_name()
    # if file_name:
    #     file_name = re.sub(r'/home/[a-zA-Z0-9]+[^/]', '~', file_name)
    #     message = os.path.dirname(file_name)[-40:] + '/'

    try:
        paths = view.window().folders()
        for path in paths:
            message = path.split('/')[-1]
    except (AttributeError, TypeError) as e:
        pass

    # paths = view.window().folders()  # /home/chrx/.../folder
    # if paths:
    #     for path in paths:
    #         message = path.split('/')[-1] + ', ' + message

    view.set_status('a_status', message)


class DefaultStatus(sublime_plugin.EventListener):

    def on_selection_modified_async(self, view):
        _set_status(view)

    def on_activated(self, view):
        _set_status(view)
