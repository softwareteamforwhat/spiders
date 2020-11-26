# -*- coding: utf-8 -*-

from scrapy import signals
from w3lib.http import basic_auth_header
import random

class ProxyDownloaderMiddleware:

    def process_request(self, request, spider):
        proxy = "tps138.kdlapi.com:15818"
        request.meta['proxy'] = "http://%(proxy)s" % {'proxy': proxy}
        # 用户名密码认证
        request.headers['Proxy-Authorization'] = basic_auth_header('t10640521499894', 'ivabjaew')  # 白名单认证可注释此行
        return None

# 请求头添加随机user-agent
class RandomUserAgentMiddleware(object):

    def __init__(self, agents):
        self.agent = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            agents=crawler.settings.get('CUSTOM_USER_AGENT')
        )

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agent))