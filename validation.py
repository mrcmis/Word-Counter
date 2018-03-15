import os.path


def file_exist_validate(file: str):
    """
    returns True when file exist, False when it does not
    :param str file: file to be validated
    """
    return os.path.isfile(file)
