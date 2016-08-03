############################################################
# Dockerfile for a Scrapy development environment
# Based on Ubuntu Image
############################################################

FROM ubuntu:14.04
MAINTAINER frank <me@lijingpeng.org>

# RUN echo deb http://mirrors.aliyun.com/ubuntu trusty universe >> /etc/apt/sources.list
RUN echo deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse >> /etc/apt/sources.list
RUN echo deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse >> /etc/apt/sources.list
RUN apt-get update

## Python Family
RUN apt-get install -qy python python-dev python-distribute python-pip ipython

## Selenium 
RUN apt-get install -qy firefox xvfb 
RUN pip install selenium pyvirtualdisplay

## AWS Python SDK
RUN pip install boto3

## Scraping
RUN pip install beautifulsoup4 requests 
RUN apt-get install -qy libffi-dev libxml2-dev libxslt-dev lib32z1-dev libssl-dev

## Scrapy
RUN pip install lxml scrapy scrapyjs
