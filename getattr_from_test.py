#xiaorui.cc
import test_for_getattr

import multiprocessing

def run(func, *args):
    print getattr(test_for_getattr, func)(*args)

#run("hello", ("hello", "world"))
print getattr(test_for_getattr, "hello")("hello", "world")
