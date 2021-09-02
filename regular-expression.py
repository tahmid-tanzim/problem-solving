#!/usr/bin/python3

import re


def main():
    project = 0
    promise = 0
    lines = open('wap.txt', 'r')
    for line in lines:
        match = re.search('pro(ject|mise)', line)
        if match:
            group = match.group()
            if group == 'project':
                project += 1
            else:
                promise += 1
    print("Promise: {} | Project: {}".format(promise, project), end='\t')


if __name__ == "__main__": main()