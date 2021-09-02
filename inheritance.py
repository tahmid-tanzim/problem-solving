#!/usr/bin/python3


class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self, upto):
        while self.b < upto:
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b


f = Fibonacci(0, 1)
for r in f.series(100):
    # if r > 100:
    #     break
    print(r, end=' ')
