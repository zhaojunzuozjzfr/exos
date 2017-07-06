#coding:utf-8
from random import shuffle, random, sample
import traceback

from dpark import DparkContext

dp = DparkContext('mesos')

'''shuffle不返回数据值'''
rdd1 = dp.parallelize([[(1,2), (3,4), (5,6)]]).map(lambda x: shuffle(x))
print 'rdd1:'
print rdd1.take(1)

rdd2 = dp.parallelize([((1, 2), (3, 4), (5, 6))]).map(lambda x: shuffle(x))
print 'rdd2:'
try:
    print rdd2.take(1) 
except Exception, e:
    print traceback.print_exc()

'''O(NlogN)'''
rdd3 = dp.parallelize([[(1,2), (3,4), (5,6)]]).map(lambda x: sorted(x, key = lambda k: random()))
print 'rdd3:'
print rdd3.take(1)

'''O(N)'''
rdd4 = dp.parallelize([[(1,2), (3,4), (5,6)]]).map(lambda x: sample(x, len(x)))
print 'rdd4:'
print rdd4.take(1)

rdd5 = dp.parallelize([((1,2), (3,4), (5,6))]).map(lambda x: sample(x, len(x)))
print 'rdd5:'
print rdd5.take(1)

rdd6 = dp.parallelize([((1,2), (3,4), (5,6))]).map(lambda x: sorted(x, key = lambda k: random()))
print 'rdd6:'
print rdd6.take(1)

