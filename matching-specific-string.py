#!/usr/bin/python3

import re

Test_String = input()

Regex_Pattern = r'hackerrank'

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
