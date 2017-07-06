#coding:utf-8

import traceback

def test(segment=0):
    try:
        len_segment = len(a) / segment
    except Exception,e:
        traceback.print_exc()
    for i in range(segment):
        print a[i*len_segment:(i+1)*len_segment]

if __name__ == '__main__':
    a = range(6)
    test(3)
    test(0)
