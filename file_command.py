import sublime, sublime_plugin
import os

class FileCommand(sublime_plugin.WindowCommand):
    """Abstract class for actions on the currently open file.

    Extends:
        sublime_plugin.WindowCommand
    """
    def description(self):
        return self.__doc__

    def is_enabled(self):
        return os.path.exists(self.window.active_view().file_name())

    def is_visible(self):
        return self.is_enabled()

    def current_path(self, relative = True):
        path = self.window.active_view().file_name()
        if not relative:
            return path
        return os.path.split(path)[1]

    def prompt_with_current_path(self, message, callback, relative = True):
        prefill = self.current_path(relative)
        prompt = self.window.show_input_panel(message, prefill, callback, None, None)
        prompt.sel().clear()
        prompt.sel().add(self.get_selection(prefill, relative))

    def get_selection(self, path, relative = True):
        name, ext = os.path.splitext(path)
        if relative:
            return sublime.Region(0, len(name))
        else:
            directory, name_with_ext = os.path.split(path)
            left_offset = len(directory) + 1
            length = len(name_with_ext) - len(ext)
            return sublime.Region(left_offset, left_offset + length)

    def ensure_parent_directory_exists(self, new_path):
        directory, file = os.path.split(new_path)
        if not os.path.isdir(directory):
            os.makedirs(directory)

    def fail_if_path_exists(self, path, message = 'Error: Target path exists'):
        if os.path.exists(path):
            self.window.status_message(message)
            raise Exception(message)
