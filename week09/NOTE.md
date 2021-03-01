学习笔记
一、使用 jango-rest-framwork
1. RESTful API 是指符合REST风格的web接口
REST设计风格：
1.  直观简洁的资源地址：URL，比如：http://example.com/resources/.
2.  传输非资源：Web服务接受与返回的互联网媒体类型，比如JSON,XML和YAML等
3.  对资源的操作：Web服务在该资源上所支持的一系列请求方法：POST\GET\PUT\DELETE
具体来说，就是把请求的实体当做资源，通过HTTP自带的方法（GET\HEAD\POST\PUT\DELETE）来进行对应的增、删、改、查等操作。比如GET请求的资源：，GET/user/可以获取用户列表，而GET/user/1可以理解为获取user id 为1的用户资源。POST请求表示新增数据，比如：POST/user/再加上body中传输的数据，用来创建一个用户。PUT请求用来更新数据，比如PUT/user/1再加上body中的数据，用来更新user id 为1的数据。同理客户DELETE 
了解了基本概念之后，我们需要了解传输数据的格式。前面说过，可以通过HTTP POST 的方法发送body数据来创建用户。那么，这个数据是什么的数据。在django-rest-framwork中默认的是JSON。但是你可以通过：HTTP请求header中的content-type来设置格式，django-rest-framewor会据此来来对应的解析。
简单来说，django-test-framework的作用等同于Django中的View+Form。我们既可以基于Model来直接生成接口，也可以自定义Serializers的字段来生成接口。
2. 接口需求及Django-rest-framwork介绍：
首先，还需要说一下需求。我们需要配置一套RESTful接口，输出左右的文章 ，其功能跟web系统提供的类似，具体包含：
1. 最新文章列表
2. 分类列表
3. 根据分类获取文章
4. 标签列表
5. 根据标签获取文章
这些都是只读功能，这样的需求在实际的项目开发中很常见。当你开发一套web系统之后，肯能需要再提供一套接口给H5端口，或者客户端用，也可能是第三方系统使用。在已经开发好的系统上开发RESTful接口，是一件十分容易的事情。但是还用提醒一下，需要权衡业务对性能的需求。
3 . 快速上手
第一步还是安装，其命令是pip install djangorestframework==3.8.2,然后把rest_framework放到INSTALLED_APPS中。
先来编写Serializer，也就是用来序列化数据的地方。在blogAapp下新增serializers.py文件，并在其中编写如下代码：
from rest_framwwork import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
class Meta:
model = Post
fields = ['title', 'category', 'desc', 'content_html', 'ceated_time'] 

  我们看到这段代码，一定会似曾相识。这跟ModelForm的写法是一致的。django-rest-framework中的Serializer跟Django的Form是等同的


