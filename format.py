# coding:utf-8

# format 通过{}和:来代替%s
print ('通过位置')
print '{0},{1}'.format('kzc', 18)
print '{},{}'.format('kzc', 18)
print '{0},{1},{0}'.format('kzc', 18), '\n'

print ('通过关键字')
print '{name},{age}'.format(name='kzc', age='18'), '\n'

print ('通过对象属性')


class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __str__(self):
        return 'This guy is {b.name}, is {b.age} old'\
                .format(b=self)


print str(Person('kzc', 18))
p = Person('kzc', 18)
print p, '\n'

print '通过下标'
p = ['kzc', 18]
print '{0[0]}, {0[1]}'.format(p), '\n'

print '填充与对齐'
print '{:>8}'.format('189')
print '{:0>8}'.format('189')
print '{:a>8}'.format('189'), '\n'

print '精度与类型f'
print '{:>.2f}'.format(233.222222), '\n'

print '金额的千分位风格符'
print '{:,}'.format(1234567890), '\n'

print '百分比表示'
print '{:.2%}'.format(19.5 / 20), '\n'

print '为数字加点号'
print '{:,}'.format(1234567890)

print '时间格式化'
import datetime
today = datetime.datetime.today()
print '{:%Y-%m-%d %H:%M:%S}'.format(today)
print '{:%Y-%m-%d}'.format(today)
