import os
import shutil
from .file_command import FileCommand

class MoveFileCommand(FileCommand):
    """Move the currently open file to another location

    Extends:
        FileCommand
    """
    def callback(self, new_path):
        self.fail_if_path_exists(new_path)
        self.ensure_parent_directory_exists(new_path)

        shutil.move(self.current_path(relative=False), new_path)
        self.window.active_view().retarget(new_path)

    def run(self):
        self.prompt_with_current_path('Move to:', self.callback, relative=False)
