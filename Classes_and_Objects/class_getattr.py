#!/usr/bin/python

class Xiaorui:

    def __init__(self):
        self.name = 'fengyun'

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, i'm %s" % self.name

foo = Xiaorui()

print hasattr(foo, 'setName')
print getattr(foo, 'name', 'NA')
print getattr(foo, 'age', 'NA')
print setattr(foo, 'age', '18')
print setattr(foo, 'work', 'student')
print setattr(foo, 'work', 'not find')
print delattr(foo, 'name')
print getattr(foo, 'name', 'not find')

