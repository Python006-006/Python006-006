#--*--encoding:utf-8--*--

import requests 
import sys
from pathlib import *
from lxml import etree
from time import sleep

def get_answer_name(url_address):

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    header = {'user-agent':user_agent}

    response = requests.get(url_address,headers = header)

    selector = etree.HTML(response.text)

    # 获取问题答案的人的名字
    # answer    = selector.xpath('//div[@class ="List-item"]/div/div/div//text()')
    author = selector.xpath('//div[@class="List-item"]//a[@class="UserLink-link"]/text()')
    answer = selector.xpath('//div[@class="List-item"]//div[@class="RichContent-inner"]/span[1]/p/text()')

    answer_info = dict(zip(author, answer))
    for i in answer_info:
        print(f'答案作者： {i} \t\t 答案内容： {answer_info[i]}')

    try :
        response = requests.get(url_address,headers = header)
    except Exception as e :
        print(e)


    # 下载信息写入文件

    ## 获取当前文件所在的目录
    basefile = Path(__file__)
    ## 获取父级mul
    file_parent = basefile.resolve().parent

    ##新建目录
    new_path = file_parent.joinpath('html_down')

    if not new_path.is_dir() :
        Path.mkdir(new_path)

    page_name = new_path.joinpath('zhihu.html')

    print(page_name)
    # sys.exit(0)

    try:
        with open(page_name,'w', encoding= 'utf-8') as files:
            files.write(str(answer_info))
    except FileNotFoundError as e:
        print(e)
    except Exception as ee:
        print(ee)

if __name__ == '__main__' :

    url_address = 'https://www.zhihu.com/question/289599760'

    get_answer_name(url_address)

    sleep(5)
