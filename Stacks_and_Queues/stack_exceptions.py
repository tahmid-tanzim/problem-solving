#!/usr/bin/python3


class FullStackException(Exception):
    """Raised when the stack is full"""
    pass


class EmptyStackException(Exception):
    """Raised when the stack is empty"""
    pass


class StackIndexOutOfRangeException(Exception):
    """Raised when the stack index is out of bound"""
    pass
