# -*- coding:utf-8 -*-
import re
import requests

class CheckIp():

    def __init__(self):
        self.local = ''
        self.http_check_url = 'http://ddns.oray.com/checkip'
        self.http_check_urls = ['http://ddns.oray.com/checkip','www.baidu.com','http://www.sina.com.cn','http://www.sohu.com']
        self.https_check_urls = ['https://ddns.oray.com/checkip', 'https://www.douban.com','https://www.tmall.com', 'https://www.jd.com']


    def _get_loacl(self):

        req = requests.get(self.http_check_url)
        self.local = self.

    def _extract_ip(self, page):
        pattern = re.compile(r'<body>Current IP Address:(\d+.\d+.\d+.\d+)<body>')
        res = re.findall(pattern=pattern, string=page)
        if len(res) >= 1:
            return res[0]

    def _extract_ip_2(self,dic):
