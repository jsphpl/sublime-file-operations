import os
import shutil
from .file_command import FileCommand

class DuplicateFileCommand(FileCommand):
    """Duplicate the currently open file to a new path

    Extends:
        FileCommand
    """
    def callback(self, new_path):
        self.fail_if_path_exists(new_path)
        self.ensure_parent_directory_exists(new_path)

        shutil.copy(self.current_path(relative=False), new_path)
        self.window.active_view().retarget(new_path)

    def run(self):
        self.prompt_with_current_path('Copy to:', self.callback, relative=False)
