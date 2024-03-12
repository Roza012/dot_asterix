"""
Purpose: Print the line that contain Z.
Auther: Roza Hadid
Date: 12.3.2024
"""
import re


def get_z_row(file_path):
    """
    Gets file path and read it, searching the line that contain Z and return it.
    :param file_path:
    :return: The line that have Z in it.
    """
    with open(file_path, "r") as my_file:
        contain = my_file.read()
    row_contain_z = re.search(".*Z.*\n", contain)
    return row_contain_z.group()
