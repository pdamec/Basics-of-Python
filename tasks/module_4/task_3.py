"""Module4/Task3: File Crawler."""
import os
from shutil import copyfile

# Vars
EXTENSIONS = ['.jpg', '.ini']
SOURCE_DIR = 'resources/task_3'
TARGET_DIR = 'resources/task_3/output'


def find_and_copy_files_with_extension(src_dir: str, dst_dir: str, extensions: list = None):
    """Find files with given extension and copy to a target location.

    :param src_dir:    root directory for walking the file tree.
    :param dst_dir:    destination folder to which found files will be copied.
    :param extensions: desired extension of a files to copy.
                       By default, if not provided, copy all files.
    """
    for root, _, files in os.walk(src_dir):
        for file in files:
            if not extensions or os.path.splitext(file)[1] in extensions:
                os.makedirs(dst_dir, exist_ok=True)
                copyfile(os.path.join(root, file),
                         os.path.join(dst_dir, file))


if __name__ == '__main__':
    find_and_copy_files_with_extension(SOURCE_DIR, TARGET_DIR, EXTENSIONS)
