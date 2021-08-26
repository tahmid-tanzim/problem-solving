#!/usr/bin/python3

def isPalindrome(input: str) -> bool:
    if len(input) <= 1:
        return True
    if input[0] == input[-1]:
        return isPalindrome(input[1:len(input) - 1])
    return False

def loop(n):
    if n == 1:
        return 1
    print(f'Before - n:{n}')
    prev = loop(n - 1)
    print(f'After - n:{n} | prev:{prev}')
    return n + prev


def list_sum(a_list):
    if len(a_list) == 0:
        return 0

    return a_list[0] + list_sum(a_list[1:])


def multiply_recursive(n, a):
    if a == 1:
        return n
    return n + multiply_recursive(n, a - 1)


def exp_recursive(n, a):
    if a == 1:
        return n
    return n * exp_recursive(n, a - 1)


def recursive_str_length(s):
    if s == '':
        return 0
    return 1 + recursive_str_length(s[1:])


def show_middle_recursive(array, min_height=[]):
    n = len(array)
    if n == 0:
        return min_height
    elif n == 1:
        print(f'Only Value - {array[0]}')
        min_height.append(array[0])
        return min_height

    middle_index = n // 2
    print(f'Middle Value - {array[middle_index]}')
    min_height.append(array[middle_index])
    show_middle_recursive(array[:middle_index])
    show_middle_recursive(array[middle_index + 1:])
    return min_height


if __name__ == "__main__":
    # print(loop(10))
    # print(list_sum([2, 3, 5, 7]))
    # print(multiply_recursive(4, 5))
    # print(exp_recursive(5, 3))
    # print(recursive_str_length('My Name is'))
    # print(show_middle_recursive([1, 2, 5, 7, 10, 13, 14, 15, 22]))
    # print(show_middle_recursive([]))

    print("kayak", isPalindrome("kayak"))
    print("abba", isPalindrome("abba"))
    print("banana", isPalindrome("banana"))

    t = [2, 0, 1, 4, 3, 3]
    for i, v in enumerate(t):
        print(f'Index - {i} & Value - {v}')
