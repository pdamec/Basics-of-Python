"""Module2/task2: custom, python split function."""
import re
import pytest

# Vars
EMPTY_STRING_ERROR = 'Please provide a valid separator. It cannot be an empty string.'


# Test data
TEST_DATA_SET_1 = [
    ('Python', ' '),
    ('Python is cool', ' '),
    (',,,,', ','),
    ('Python', 'Javascript')
                   ]

# my_split(“Python is cool”, ‘ ‘) -> [‘Python’, ‘is’, ‘cool’]
# my_split(",,,,", ',') -> ['', '', '', '', '']
# my_split("Python", "Javascript") -> ['Python']


def my_split(string_to_split, sep=None) -> list:
    """Python's implementation of builtin (C) split function.
    """
    if sep == '':
        raise ValueError(EMPTY_STRING_ERROR)
    elif sep is None:
        sep = ' '
        string_to_split = re.sub(r'[ \s]+', ' ', string_to_split)

    split_results = []
    tmp_str = ''

    for char in string_to_split:
        tmp_str += char
        if tmp_str.find(sep) != -1:
            split_results.append(tmp_str[0:len(tmp_str) - len(sep)])
            tmp_str = ""
    split_results.append(tmp_str)
    return split_results


@pytest.mark.parametrize("text_to_split,sep",
                         [TEST_DATA_SET_1])
def test_my_split(text_to_split, sep):
    assert my_split(text_to_split, sep) == text_to_split.split(sep)


