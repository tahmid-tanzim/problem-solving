#!/usr/bin/python3


class InclusiveRange:
    def __init__(self, *args):
        length = len(args)
        if length < 1:
            raise TypeError('requires at least one arguments, got {}'.format(length))
        elif length == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif length == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif length == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('expected at most 3 arguments, got {}'.format(length))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main():
    for i in InclusiveRange(5, 25, 2):
        print(i, end=' ')


if __name__ == "__main__": main()