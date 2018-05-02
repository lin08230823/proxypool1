#-*- coding:utf-8 -*-
import requests
import time
from selenium import webdriver
from myproxy.models import Proxy
from myproxy.utils.checkip import CheckIp

# 初始化
checkip = CheckIp()

class GeneralMethods():

    def __init__(self):

        self.all_items = Proxy.objects.all()

    def save_proxy(self,resource,ip,port,head,district='其他',http_type='O'):
        '''Verifies and saves a IP

        resource: which website this IP comes form
        ip: IP in string
        port: IP port
        head: IP head, http or https
        district: where this IP's location
        http_type:  which type this IP is, 'O' stands for 其他 , 'G' for 高匿， ‘T’ for 透明

        '''
        try:
            query = self.all_items.get(ip=ip)
            return
        except:
            pass

        #不验证直接储存
        Proxy.objects.create(
            resource=resource,
            ip=ip,
            port=port,
            head=head,
            status='V',
            district=district,
            type=http_type
            )



    def get_cookie_by_selenium(self, url):


        driver = webdriver.PhantomJS()
        driver.get(url)
        cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookie()]
        cookiestr = ';'.join(item for item in cookie)
        driver.quit()
        return cookiestr


    def get_source_by_selenium(self, url):

        driver = webdriver.PhantomJS()
        driver.get(url)

        page_state = ''
        while True:
            page_state = driver.execute_script('return document.readyState;')
            if page_state == 'compete':
                break
            time.sleep(3)

        return driver.page_source

    def req_url(self,url, headers, req_count=1):
        try :
            req = requests.get(url, headers=headers, timeout=2)
            assert req.status_code == 200
        except Exception as e:
            if req_count == 1:
                cookies = self.get_cookie_by_selenium(url)
                headers['Cookies'] = cookies
                return self.req_url(url, headers, req_count=2)
            else:
                print('url : %s 第二次报错, 报错信息: %s, 已转为 selenium 获取页面信息').format(url, e)
                return None

        else:
            return req.text
