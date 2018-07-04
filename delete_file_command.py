import os
from .file_command import FileCommand

class DeleteFileCommand(FileCommand):
    """Delte the currently open file

    Extends:
        FileCommand
    """
    def run(self):
        os.unlink(self.current_path(relative = False))
        self.window.run_command('close_file')
