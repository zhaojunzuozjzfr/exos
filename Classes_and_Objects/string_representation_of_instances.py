# coding:utf-8


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!r}, {0.y!s})'.format(self)


p = Pair(3, 4)

p
# out of __repr__: Pair(3, 4)

print p
# (3, 4)

print('p is {0!r}'.format(p))
# p is Pair(3, 4)

print('p is {0}'.format(p))
# p is (3, 4)
