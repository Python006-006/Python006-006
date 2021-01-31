# 作业二：在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，
# 请基于 Python 和 redis 实现如下的短信发送接口：
# 已知有如下函数：
import redis
import time
client = redis.Redis(host = '127.0.0.1', password = '')

def sendsms(telephone_number: int, content: string, key=None):
    # 短信发送逻辑, 作业中可以使用 print 来代替
    # 计算手机发送的次数

    client.set(telephone_number, '0', nx=True)
    print(content)
    count_number = client.incr(telephone_number)
    #计算时间
    start_time = time.time()
    client.set(telephone_number, start_time, nx=True)


    
    # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后
    pass
    print("发送成功")