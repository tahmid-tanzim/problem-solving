#!/usr/bin/python3
# https://www.algoexpert.io/questions/Valid%20IP%20Addresses
"""
  You're given a string of length 12 or smaller, containing only digits. Write a
  function that returns all the possible IP addresses that can be created by
  inserting three .s in the string.

  An IP address is a sequence of four positive integers that are separated by
  .s, where each individual integer is within the range
  0 - 255, inclusive.

  An IP address isn't valid if any of the individual integers contains leading
  0s. For example, "192.168.0.1" is a valid IP
  address, but "192.168.00.1" and
  "192.168.0.01" aren't, because they contain "00" and
  01, respectively. Another example of a valid IP address is
  "99.1.1.10"; conversely, "991.1.1.0" isn't valid,
  because "991" is greater than 255.

  Your function should return the IP addresses in string format and in no
  particular order. If no valid IP addresses can be created from the string,
  your function should return an empty list.

  Note: check out our Systems Design Fundamentals on SystemsExpert to learn more
  about IP addresses!

Sample Input
string = "1921680"

Sample Output
[
  "1.9.216.80",
  "1.92.16.80",
  "1.92.168.0",
  "19.2.16.80",
  "19.2.168.0",
  "19.21.6.80",
  "19.21.68.0",
  "19.216.8.0",
  "192.1.6.80",
  "192.1.68.0",
  "192.16.8.0"
]
// The IP addresses could be ordered differently.
"""


# Time Complexity - O(1)
# Space Complexity - O(1)
def validIPAddresses(string):
    IP_ADDRESS = list()

    # Calculate First Segment
    char = ''
    for i in range(len(string)):
        if char == '0':
            break
        char += string[i]
        if 0 <= int(char) <= 255:
            IP_ADDRESS.append([char, string[i + 1:]])
        else:
            break

    # Calculate Second Segment
    j = 0
    n = len(IP_ADDRESS)
    while j < n:
        element = IP_ADDRESS.pop(0)
        char = ''
        for i in range(len(element[1])):
            if char == '0':
                break
            char += element[1][i]
            if 0 <= int(char) <= 255:
                IP_ADDRESS.append([element[0] + "." + char, element[1][i + 1:]])
            else:
                break
        j += 1

    # Calculate last half Third & Fourth Segment
    j = 0
    n = len(IP_ADDRESS)
    while j < n:
        element = IP_ADDRESS.pop(0)
        first_half = element[0]
        last_half = element[1]
        i = 1
        while i < len(last_half):
            third_segment = last_half[0:i]
            fourth_segment = last_half[i:len(last_half)]
            if 0 <= int(third_segment) <= 255 and 0 <= int(fourth_segment) <= 255 and not (
                    len(third_segment) > 1 and third_segment[0] == '0' or len(fourth_segment) > 1 and fourth_segment[
                0] == '0'):
                IP_ADDRESS.append(first_half + "." + third_segment + "." + fourth_segment)
            i += 1
        j += 1
    return IP_ADDRESS


if __name__ == '__main__':
    output1 = validIPAddresses("1921680")
    print(f'{output1}')
