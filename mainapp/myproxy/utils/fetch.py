#-*- coding:utf-8 -*-

import threading

from ..spiders import xici, sixsix, kuaidaili, ip181


XICI = xici.fetch_xici
SIXSIX = sixsix.fetch_ss
KUAIDAILI = kuaidaili.fetch_k1
IP181 = ip181.ip181


# 多线程
funcs = [XICI,SIXSIX,KUAIDAILI,IP181]

def crawl():

    print('crawling')

    threads = []
    for i in range(len(funcs)):
        t = threading.Thread(target=funcs[i])
        threads.append(t)
    for i in range(len(funcs)):
        threads[i].start()
    for i in range(len(funcs)):
        threads[i].join()

    print('finished')



    


