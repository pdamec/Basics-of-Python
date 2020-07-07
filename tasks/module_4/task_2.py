"""Module4/task2: File Extension Handler."""
import os
from contextlib import contextmanager


FILE_PREFIX = 'spam'


@contextmanager
def cwd(new_dir):
    old_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(old_dir)


def get_files_with_prefix() -> list:
    """Get files with a specified prefix.

    :return list of files matching a given prefix.
    """
    matching_files = []
    for file_ in os.listdir():
        if os.path.isfile(file_) and file_.startswith(FILE_PREFIX):
            matching_files.append(file_)
    return matching_files


def adjust_files(files: list):
    """Rename file to match ordering pattern.

    :param files: list of files to adjust.
    """
    extensions = set(os.path.splitext(file_)[1] for file_ in files)
    for extension in extensions:
        index = 1
        for file_ in sorted(files):
            if extension in file_:
                new_file = f'{FILE_PREFIX}{index:03}{extension}'
                os.rename(file_, new_file)
                index += 1


if __name__ == '__main__':
    files_dir = 'resources/task_2'

    with cwd(files_dir):
        files_with_prefix = get_files_with_prefix()
        adjust_files(files_with_prefix)
