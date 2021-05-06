#!/usr/bin/python3


class Node:
    def __init__(self, name, children=[], state=None):
        self.name = name
        self.children = children
        self.state = state

    def __str__(self):
        return f'Node {self.name} {self.state}'

    def __eq__(self, val):
        return self.name == val

    def getName(self):
        return self.name

    def addChildren(self, child):
        self.children = self.children + [child]

    def getChildren(self):
        return self.children

    def printChildren(self):
        return [child.__str__() for child in self.children]

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def isState(self, state):
        return self.state == state
