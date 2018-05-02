# -*- coding:utf-8 -*-

import bs4

from myproxy.spiders import general_methods

gm = general_methods.GeneralMethods()

headers_general = {
    'User-Agent': '"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) '
    'AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",',
}


# 本次爬取内查重
XICI_IP = []

def fetch_xici():
    '''从西刺网下载ip'''
    urls = ['http://www.xicidaili.com/nn/',
            'http://www.xicidaili.com/nt/',
            'http://www.xicidaili.com/wn/',
            'http://www.xicidaili.com/wt/']
    for url in urls:
        content = gm.req_url(url, headers_general)
        if not content:
            try:
                content = gm.get_source_by_selenium(url, headers_general)
            except Exception as e:
                print(e)
                return None
        try:
            soup = bs4.BeautifulSoup(content, 'lxml')
            # 筛选出所有包含 ip 的 tr 标签
            tr_list = soup.find_all('tr', attrs={'class': ['odd', '']})
            for tr in tr_list:
                soup_td = tr.find_all('td')

                ip = soup_td[1].string
                port = soup_td[2].string

                district = soup_td[3].get_text()
                if district:
                    district = district.strip()

                http_type = soup_td[4].string
                http_head = soup_td[5].string

                if '高匿' in http_type:
                    type = 'G'
                elif '透明' in http_type:
                    type = 'T'
                else:
                    type = 'O'

                if ip in XICI_IP:
                    continue
                XICI_IP.append(ip)
                print('===============',ip,port,http_head,district,type,'===============')
                gm.save_proxy(resource='西刺',ip=ip, port=port, head=http_head, district=district, http_type=type)
                print('------')
        except Exception as e:
            print('error happened when request url:{0},error info:{1}'.format(url,e))

