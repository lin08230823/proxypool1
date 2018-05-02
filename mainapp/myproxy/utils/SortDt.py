from myproxy.models import Proxy

def deduplicate():

    all_ip = Proxy.objects.filter(status='V')
    list_ip = []
    count = 0
    for ip in all_ip:
        print(ip.ip)
        if ip.ip in list_ip:
            count += 1
            ip.delete()
        list_ip.append(ip.ip)

    return count

def delete():
    all_ip = Proxy.objects.filter(failed_time__gte=5)
    all_ip.delete()

    return len(all_ip)

def sort():
    print('deduplicating proxies')
    deduplicate_count = deduplicate()
    delete_count = delete()
    print('deduplicated {0} items, delete {1} invaild ip .'.format(deduplicate_count, delete_count))
