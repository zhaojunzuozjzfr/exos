#coding:utf-8

def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))

def add_to(num, target=None):
    if target is None:
        target = []
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))
