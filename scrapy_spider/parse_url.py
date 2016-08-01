# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import sys
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

cnt = 1
def parse(url):
    result = {
        'content':'',
        'source':'',
        'author':'',
        'createTime':'',
        'remarkCnt':''
    }
    page = urllib2.urlopen(url).read()
    content = bs(page, from_encoding='gbk')
    s = ''
    rs = content.findAll(attrs={"id": "Cnt-Main-Article-QQ"})
    for i in rs:
        s = s+i.text
    source = content.find(attrs={"class": "a_catalog"}).text
    author = content.find(attrs={"class": "a_source"}).text
    createTime = content.find(attrs={"class": "a_time"}).text
    remarkCnt = content.find(attrs={"class": "a_commentNum"}).text

    result['source'] = source.encode('utf-8')
    result['author'] = author.encode('utf-8')
    result['createTime'] = createTime.encode('utf-8')
    result['remarkCnt'] = remarkCnt.encode('utf-8')
    result['content'] = s.encode('utf-8')

    return result

if __name__ == '__main__':
    print parse("http://finance.qq.com/a/20160726/020741.htm")