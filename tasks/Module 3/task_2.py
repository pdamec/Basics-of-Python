"""Module2/task2: custom, python split function."""
import re
import pytest

# Vars
EMPTY_STRING_ERROR = 'Please provide a valid separator. ' \
                     'It cannot be an empty string.'


# Test data
TEST_DATA_SET_1 = [
    ('Python is cool', ' ', ['Python', 'is', 'cool']),
    (',,,,', ',', ['', '', '', '', '']),
    ('Python', 'Javascript', ['Python'])
]
TEST_DATA_SET_2 = [
    ('feuer DPS pew pew', '')
]


def my_split(string_to_split, sep=None) -> list:
    """Python's implementation of builtin (C) split function.

    :param string_to_split: string that shall be splitted.
    :param sep: separator by which string is splitted. None equals ' '
    """
    if sep == '':
        raise ValueError(EMPTY_STRING_ERROR)

    if sep is None:
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


# Tests
@pytest.mark.parametrize("text_to_split,sep,expected_result", TEST_DATA_SET_1)
def test_expected_my_split(text_to_split, sep, expected_result):
    """Test if my_split function returns the expected values."""
    assert my_split(text_to_split, sep) == expected_result


@pytest.mark.parametrize("text_to_split,sep", TEST_DATA_SET_2)
def test_empty_sep_my_split(text_to_split, sep):
    """Test if my_split function raises ValueError when no separator is provided."""
    with pytest.raises(ValueError, match=EMPTY_STRING_ERROR):
        my_split(text_to_split, sep)
