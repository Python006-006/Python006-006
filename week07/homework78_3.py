'''
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
'''
import time 

def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return inner

@timer
def func(a, b):
    return a + b 

func(3, 5)