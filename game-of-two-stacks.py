#!/usr/bin/python3
# https://www.hackerrank.com/challenges/game-of-two-stacks/problem


def find_sum(str1, str2):
    # Before proceeding further,
    # make sure length of str2 is larger.
    if len(str1) > len(str2):
        t = str1
        str1 = str2
        str2 = t

    # Take an empty string for
    # storing result
    str_final = ""

    # Calculate length of both string
    n1 = len(str1)
    n2 = len(str2)

    # Reverse both of strings
    str1 = str1[::-1]
    str2 = str2[::-1]

    carry = 0
    for i in range(n1):
        # Do school mathematics, compute
        # sum_all of current digits and carry
        sum_all = ((ord(str1[i]) - 48) +
               ((ord(str2[i]) - 48) + carry))
        str_final += chr(sum_all % 10 + 48)

        # Calculate carry for next step
        carry = int(sum_all / 10)

        # Add remaining digits of larger number
    for i in range(n1, n2):
        sum_all = ((ord(str2[i]) - 48) + carry)
        str_final += chr(sum_all % 10 + 48)
        carry = (int)(sum_all / 10)

        # Add remaining carry
    if carry:
        str_final += chr(carry + 48)

        # reverse resultant string
    str_final = str_final[::-1]

    return str_final


def two_stacks(x, a, b):
    total, count, i, j = 0, 0, 0, 0
    while total <= x:
        if i < len(a) and j < len(b):
            if a[i] >= b[j]:
                # total += b[j]
                total = int(find_sum(str(total), str(b[j])))
                j += 1
            else:
                # total += a[i]
                total = int(find_sum(str(total), str(a[i])))
                i += 1
            count += 1
        elif i < len(a) and j >= len(b):
            count += 1
            # total += a[i]
            total = int(find_sum(str(total), str(a[i])))
            i += 1
        elif j < len(b) and i >= len(a):
            count += 1
            # total += b[j]
            total = int(find_sum(str(total), str(b[j])))
            j += 1
        else:
            count += 1
            break
    return count - 1 if count > 1 else 0


if __name__ == '__main__':
    for k in range(35):
        print(k, '--', two_stacks(k, [4, 2, 4, 6, 1], [2, 1, 8, 5]))
