# -*- coding:utf-8 -*-
import requests
from 爬虫.UserAgent_demo import UserAgent
import random
from lxml import etree
import re
USER = UserAgent()
headers = {
    'Referer': 'http://www.bookschina.com/',
    'Host': 'www.bookschina.com',
    'User-Agent': random.choice(USER.getuseragent())
}
req = requests.get('http://www.bookschina.com/',headers=headers)
html = etree.HTML(req.text)
urls = html.xpath('//p[@class="mcate-item-bd"]//a/@href')
for i in range(len(urls)):
    if urls[i] =='/kinder/53210000/':
        print(i)
