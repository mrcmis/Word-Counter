import config


def count_lines(file: str):
    """
    :param str file: file to be checked
    """
    count = 0
    with open(file) as f:
        for line in f:
            count = count + 1
    return count


def count_chars(file):
    """
    counting characters in file, characters
    from config.py not_char list are not taken under consideration
    not_char is empty by default
    :param str file: file to be checked
    """
    count = 0
    with open(file) as f:
        for line in f:
            for ch in line:
                if ch not in config.non_char:
                    count = count + 1
    return count


def count_words(file):
    """
    counting words in file, assuming that words are separated by
    special characters - (' ',',','.' by default). Special characters
    may be set in config.py
    :param str file: file to be checked
    """
    count = 0
    with open(file) as f:
        is_white = True
        for line in f:
            is_white = False
            for ch in line:
                if ch not in config.white_spaces:
                    is_white = False
                else:
                    if not is_white:
                        count = count+1
                        is_white = True
        if not is_white:
            count = count + 1
    return count
