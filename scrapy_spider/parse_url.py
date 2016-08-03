# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import sys
import urllib2
import re

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
    [s.extract() for s in content('style')]
    [s.extract() for s in content('script')]

    s = ''
    rs = content.findAll(name = 'p', attrs = {'style':re.compile(r'TEXT-INDENT: 2em')})
    if rs is None:
        return None
    for i in rs:
        s = s + i.text

    source = ''
    author = ''
    createTime = ''
    remarkCnt = ''
    try:
        source = content.find(attrs={"class": "a_catalog"}).text
        author = content.find(attrs={"class": "a_source"}).text
        createTime = content.find(attrs={"class": "a_time"}).text
        remarkCnt = content.find(attrs={"class": "a_commentNum"}).text
    except AttributeError:
        pass

    result['source'] = source.encode('utf-8').strip('\n')
    result['author'] = author.encode('utf-8').strip('\n')
    result['createTime'] = createTime.encode('utf-8').strip('\n')
    result['remarkCnt'] = remarkCnt.encode('utf-8').strip('\n')
    result['content'] = s.encode('utf-8').strip('\n')

    return result

if __name__ == '__main__':
    print parse("http://cd.qq.com/a/20160615/010352.htm")
