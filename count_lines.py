"""
Purpose: Return the number of lines in file.
Auther: Roza Hadid
Date: 12.3.2024
"""
import re


def count_lines(file_path):
    """
    Gets file path and opened it.
    Then put in a list all the \n that found in the file and return the length of this list.
    :param file_path: A path of a file.
    :return: How many lines the file contains.
    """
    with open(file_path, "r") as my_file:
        contain = my_file.read()
    number_of_lines = re.findall("\n", contain)
    return len(number_of_lines)
