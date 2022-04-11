#!/usr/bin/python3
# https://leetcode.com/problems/excel-sheet-column-title/


def convertToTitle(column_number: int) -> str:
    column_title = str()

    while column_number > 0:
        char_index_value = 26 if column_number % 26 == 0 else column_number % 26
        column_title = chr(char_index_value + 64) + column_title
        column_number -= char_index_value
        column_number = column_number // 26

    return column_title


if __name__ == "__main__":
    print(convertToTitle(1))  # "A"
    print(convertToTitle(28))  # "AB"
    print(convertToTitle(701))  # "ZY"
    print(convertToTitle(2147483647))  # "FXSHRXW"

