#!/usr/bin/python3

lines = open('wap.txt', 'r')
for line in lines.readlines():
    print(line, end='\t')

