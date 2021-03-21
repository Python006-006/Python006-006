学习笔记
#使用requests库获取豆瓣影评
#使用BeautifulSoup解析网页
'''
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
猫眼电影网址：https://maoyan.com/films?showType=3
'''
import requests
from  bs4 import BeautifulSoup as bs 
#bs4是第三方的库，需要使用pip安装

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

# myurl = 'http://i.chinastock.com.cn'

response = requests.get(myurl, headers=header)

# print(response.text)
# print(f'返回码是:{response.status_code}')

bs_info = bs(response.text, 'html.parser') # html.parser 是解析器

#python 中使用for in 形式的循环，python 使用缩进来做语句块的分割
print('*'*40)
for tags in bs_info.find_all('dl', attrs={'class': 'movie-list'}):
    print(tags)
    for atag in tags.find_all('dd', ):

        print(atag.find('href').text)
        #获取所有的链接
        print(atag.find('span',attrs={'class': 'name'}).text)
        #获取电影名称////