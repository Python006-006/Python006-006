#--*--encoding:utf-8--*--

#1 练习：random..
from random  import *
#生成伪（和时间戳有关）随机数：0~1的浮点数
print(random())
#升级随机数：整数
print(randrange(0,11,2))
#随机抽取一个元素
print(choice(['reb','black','orange']))
#随机抽取多个元素
print(sample([1,2,3,4,5,6], k = 4))

#2 练习：json编解码
import json

a = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(a)

b = json.dumps("['foo', {'bar': ['baz', None, 1.0, 2]}]")
print(b)

# 3 练习：路径处理

from pathlib import Path

p = Path()
print(p.resolve())