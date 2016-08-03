# scrapy_spider
Scrapy爬虫示例

本地化执行：  
> scrapy crawl qq_search_spider

容器化
-----
如果你在本地安装scrapy的时候遇到了一堆环境依赖问题，例如openssl问题、zope问题等，那么建议你在docker中运行scrapy，请参考：
https://github.com/lijingpeng/scrapy-development-docker

具体操作步骤如下（首先确保你已经安装了docker）：  
```bash
# 1. 编译  
docker build -t scrapy .
# 2. 进入容器, 注：-v 参数映射本地代码到容器中
docker run -v ~/scrapy_spider:/opt/dev -it scrapy  /bin/bash
# 3. 执行  
scrapy crawl qq_search_spider
```
