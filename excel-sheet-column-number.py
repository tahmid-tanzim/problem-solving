#!/usr/bin/python3
# https://leetcode.com/problems/excel-sheet-column-number/


def title_to_number(column_title: str) -> int:
    column_number = 0
    n = len(column_title) - 1
    for char in column_title:
        char_index_value = ord(char) - 64
        column_number += (26 ** n) * char_index_value
        n -= 1
    return column_number


if __name__ == "__main__":
    print(title_to_number("A"))  # 1
    print(title_to_number("AB"))  # 28
    print(title_to_number("ZY"))  # 701
    print(title_to_number("FXSHRXW"))  # 2147483647

