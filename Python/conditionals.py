#!/usr/local/bin/python3.6

a, b = 0, 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is NOT less than b ({})'.format(a, b))

print('foo' if a < b else 'bar')
