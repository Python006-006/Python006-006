# 作业二：在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，
# 请基于 Python 和 redis 实现如下的短信发送接口：
# 已知有如下函数：
import redis
import time
client = redis.Redis(host = '127.0.0.1', password = '')

def sendsms(telephone_number, content, key=None):
    # 短信发送逻辑, 作业中可以使用 print 来代替

    if not client.get(telephone_number):
        client.set(telephone_number, '1', 60, nx=True)
        print('发送成功0')

    elif int(client.get(telephone_number)) < 5 :
        count_number = client.incr(telephone_number)
        print('发送成功1')

    else:
        print('1 分钟内发送次数超过 5 次, 请等待 1 分钟')

if __name__ == '__main__':
    sendsms(14725836989,'hello')
    sendsms(15936598789,'hello')

