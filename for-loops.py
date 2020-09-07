#!/usr/local/bin/python3.6

lines = open('wap.txt', 'r')
for line in lines.readlines():
    print(line, end='\t')

