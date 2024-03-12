"""
Purpose: Importing from another moduls to run them.
Auther: Roza Hadid
Date: 12.3.2024
"""
from count_lines import count_lines
from get_z_row import get_z_row


def main():
    """ Entry point """
    print(count_lines(r"C:\Users\User\Downloads\alice30.txt"))
    print(get_z_row(r"C:\Users\User\Downloads\alice30.txt"))


if __name__ == '__main__':
    main()
