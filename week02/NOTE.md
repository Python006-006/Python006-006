shift + enter :可以执行选中的代码
ctrl + 左键 ：跟踪代码
整体缩进：
tab
整体取消缩进：
tab+shift
Python strip() 方法用于移除字符串头尾指定的字符(默认为空格或换行符)或字符序列
自定义异常处理：要继承：exception，使用raise 抛出异常信息。异常信息可以嵌套。

class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    del userinput  删除变量：清理内存


类：可以当做函数或字符串使用

抛出异常美化：使用pretty_errors :
pip install pretty_errors

上下文管理器：with
file1 = open('a.txt', encoding='utf8')
try:
    data = file1.read()
finally:
    file1.close()

with open('a.txt', encoding='utf8') as file2:
    data = file2.read()

GET : 增强
payload = {'key1':'value1','key2':['value02','value03']}

response = requests.get(url_address,headers = header, params = payload )

页面分析：
Host : 主机（集群部署）
Referer：从哪里访问过来的

pip install --target=xxx pygame

问：Requirement already satisfied: lxml in c:\python37\lib\site-packages (4.5.0)

解：pip install --target=c:\python37\lib\site-packagespygame lxml
   --需要指定安装路径

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pathlib import *
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

"""
https://www.zhihu.com/api/v4/questions/26551475/root_comments?limit=10&offset=30&order=normal&status=open
使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。
https://www.zhihu.com/question/421150601
referer: https://www.zhihu.com/question/421150601
method:post
用户：//div[@class="List-item"]//a[@class="UserLink-link"]/text()
答案://div[@class="List-item"]//div[@class="RichContent-inner"]/span[1]/p/text()
答案的规则： span 标签  类class  =  "RichText ztext CopyrightRichText-richText"
"""

# starter

if __name__ == '__main__':
    driver = webdriver.Chrome()  # 打开浏览器

    driver.get("https://www.zhihu.com/question/421150601")
    time.sleep(5)
    action1 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button")
    ActionChains(driver).move_to_element(action1).click(action1).perform()

    # driver.find_element_by_id("su").click()
    # 模拟用户操作
    def execute_times(times):

        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # try:
            #     driver.find_element_by_css_selector('button.QuestionMainAction').click()
            #     print("page" + str(i))
            #     time.sleep(1)
            # except Exception as e:
            #     print(e)
            #     break

    execute_times(10)

    result_raw = driver.page_source
    with open('zhihu_yuanshi.html','w',encoding='utf-8') as f:
        f.write(result_raw)
    # print(result_raw)学习笔记