# 作业一：使用 Python+redis 实现高并发的计数器功能
# 需求描述:
# 在社交类网站中，经常需要对文章、视频等元素进行计数统计功能，热点文章和视频多为高并发请求，因此采用 redis 做为文章阅读、视频播放的计数器。
# 请实现以下函数：
import redis
client = redis.Redis(host = '127.0.0.1', password = '')

# client.incr('keys')  # +1

def counter(video_id):
    client.set(video_id, '0', nx=True)
    count_number = client.incr(video_id)
    return count_number

print(counter(1001))
print(counter(1002))
print(counter(1003))
print(counter(1005))
print(counter(1006))
print(counter(1007))