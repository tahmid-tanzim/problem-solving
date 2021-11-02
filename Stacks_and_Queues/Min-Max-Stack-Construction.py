#!/usr/bin/python3
# https://www.algoexpert.io/questions/Min%20Max%20Stack%20Construction
"""
  Write a MinMaxStack class for a Min Max Stack. The class should
  support:

  1. Pushing and popping values on and off the stack.
  2. Peeking at the value at the top of the stack.
  3. Getting both the minimum and the maximum values in the stack at any given
    point in time.

  All class methods, when considered independently, should run in constant time
  and with constant space.

Sample Usage
// All operations below are performed sequentially.
MinMaxStack(): - // instantiate a MinMaxStack
push(5): -
getMin(): 5
getMax(): 5
peek(): 5
push(7): -
getMin(): 5
getMax(): 7
peek(): 7
push(2): -
getMin(): 2
getMax(): 7
peek(): 2
pop(): 2
pop(): 7
getMin(): 5
getMax(): 5
peek(): 5
"""


class MinMaxStack:
    def __init__(self):
        self.container = []

    def peek(self):
        return self.container[-1]

    def pop(self):
        last_value = self.container[-1]
        del self.container[-1]
        return last_value

    def push(self, number):
        self.container += [number]

    def getMin(self):
        minimum_value = self.container[0]
        i = 1
        while i < len(self.container):
            if self.container[i] < minimum_value:
                minimum_value = self.container[i]
            i += 1
        return minimum_value

    def getMax(self):
        maximum_value = self.container[0]
        i = 1
        while i < len(self.container):
            if self.container[i] > maximum_value:
                maximum_value = self.container[i]
            i += 1
        return maximum_value


if __name__ == "__main__":
    pass
