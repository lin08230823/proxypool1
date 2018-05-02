# -*- coding:utf-8 -*-
import re
import requests

class CheckIp():

    def __init__(self):
        self.local = ''
        self.http_check_url = 'http://ddns.oray.com/checkip'
        self.http_check_urls = ['http://ddns.oray.com/checkip', 'http://www.baidu.com', 'http://www.sina.com.cn', 'http://www.sohu.com']
        self.https_check_urls = ['https://ddns.oray.com/checkip', 'https://www.douban.com' ,'https://www.tmall.com', 'https://www.jd.com']


    def _get_loacl(self):

        req = requests.get(self.http_check_url)
        self.local = self._extract_ip(req.text)

    def _extract_ip(self, page):
        pattern = re.compile(r'<body>Current IP Address: (\d+.\d+.\d+.\d+)</body>')
        res = re.findall(pattern=pattern, string=page)
        if len(res) >= 1:
            return res[0]

    def _extract_ip_2(self,dic):

        try:
            proxy = dic.get('http')
        except:
            proxy = dic.get('https')

        ip = proxy.split('//')[1].split(':')[0]
        return ip

    def check(self, proxy, type, is_https=False):

        if is_https:
            urls = self.https_check_urls

        else:
            urls = self.http_check_urls

        try:
            #print(urls[0],proxy)
            req = requests.get(url=urls[0], proxies=proxy, timeout=2)
            #print(req.text)
            assert req.status_code == 200
            res = self._extract_ip(req.text)
            #print(res)
            assert bool(res) == True
        except:

            return False

        for url in urls[1:]:

            try:
                req = requests.get(url=url, proxies=proxy, timeout=2)
                assert req.status_code == 200

            except Exception as e:
                print(e)
                return False
        return True
