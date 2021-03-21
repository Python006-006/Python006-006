import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import random 

user_agent = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
               "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
               "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
               "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
               "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

header = {}

header['user-agent'] = random.choice(user_agent)

def downloadHtml(url):
    try:
        response = requests.get(myurl, headers=header)

        # print(response.status_code)
        # print(response.text)

        #xml化处理

        selector = lxml.etree.HTML(response.text)

        # print(selector)

        film_link = []

        url_re = []

        film_link = selector.xpath('//dl[@class="movie-list"]/dd[i]/div[2]/a/@href')

        for i in range(30):

            film_link.append = selector.xpath('//dl[@class="movie-list"]/dd[i]/div[2]/a/@href')

            # print(film_link)

            url_base = 'https://maoyan.com'

            film_link_true = ''.join(film_link)

            # print(film_link_true)

            url_re.append(url_base + film_link_true)

           # print(url_re)

        return url_re

    except:
        return ''

def parse(url):

    url_results = downloadHtml(url)

    film_info = []

    for url_result in url_results:

        response_1 = requests.get(url_result, headers=header)

        selector_1 = lxml.etree.HTML(response_1.text)

        print(selector_1)

        film_name = selector_1.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')

        print(film_name)

        film_type_result =[]
        film_type = selector_1.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
        film_type_result = film_type
        film_type_1 = selector_1.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[2]/text()')
        film_type_result.append(''.join(film_type_1))

        print(film_type_result)

        film_time = selector_1.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')

        print(film_time)

        film_info.append((film_name,film_type_result,film_time))



if __name__=='__main__':
    urls = tuple(f'https://maoyan.com/films?showType=3&offset={page*30}'for page in range(10))
    # myurl = 'https://maoyan.com/films?showType=3&offset=0'
    print(urls)
    for myurl in urls:
        parse(myurl)
