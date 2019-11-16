# encoding: utf-8
__author__ = 'liuwangxuezhang'

import requests
import re
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
 "Cookie":""}
zh_url = "https://www.zhihu.com/billboard"
zh_response = requests.get(zh_url,headers=headers)


zh_response.encoding = 'utf-8'
content = zh_response.text
# print(content.encode('gbk','ignore').decode)
html = etree.HTML(content)
print(html)
result = html.xpath('//*[@id="root"]/div/main//a')
print(len(result))
for li in result:
    try:
        num = li.xpath('./div[1]/div[1]/text()')[0]
        title = li.xpath('./div[2]/div[1]/text()')[0]
        hot = li.xpath('./div[2]/div[2]/text()')[0]
        print(num ,title,hot)

    except Exception as e:
        # 异常保存，第二天，分析，单独爬取。
        print(e)

