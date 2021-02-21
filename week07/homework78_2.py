'''
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
'''

def map_1(func,*iterators):
    try:
        i = 0
        while 1:
            yield func(*[j[i] for j in iterators])
            i += 1
    except IndexError :
        pass


def square(x) :            # 计算平方数
    return x ** 2

y = map_1(square, [1, 2, 3, 4, 5])

for i in y:
    print(i)

def add(x, y):
    return x + y 

print('*'*20)

y = map_1(add, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

for i in y:
    print(i)



