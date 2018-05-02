from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Proxy,IpAddr
from .utils.VerifyProxy import verify
from .utils.SortDt import sort
from .utils.fetch import crawl
import json
from datetime import datetime, timezone, date
# Create your views here.

#=========================== 首页 ===============================
def index(request):
    items = Proxy.objects.filter(status='V').order_by('-last_modified_time')[:50]

    contents = {
        'items': items,
    }
    return render(request, 'myproxy/index.html', contents)


#=========================== 管理页 ==============================
def manage(request):
    return render(request,'myproxy/new_index.html')

#=========================== 手动工作 ==========================

TASK = [crawl,sort,verify]
@staff_member_required()
def work(request):
    if request.method == 'GET':
        crawl()
        sort()
        verify()


        return JsonResponse({'data': 'all works done'})

# =========提取IP =========================
MAX_REQUIRED_NUM = 20
DEFAULT_NUM =5


def get(request):
    '''返回 JSON 格式的IP数据
    num - 请求的 ip 数量，
        如果不为数字，返回错误信息 'require a integer'
        如果大于限定的最大数量，则取最大的数
        如果请求的数量大于数据库中总数量，返回数据库所有 ip， 并在 status 中标明 'not enough'

    v_num - times passed verif

    type - ip type 'O' stands for 其他 ,'G' for 高匿,'T' for 透明

    head - http-head, offer two choices
            head = http or head = https

    location - where these ips' location

    '''
    # global VERIFY_STATUS

    judge = judge_request(request)
    if not judge:
        data = {}
        data['code'] = 0
        return JsonResponse(data)

    if request.method == 'GET':
        valid_ip = Proxy.objects.filter(status='V').order_by('-last_modified_time')
        num = request.GET.get('num',None)
        if num :
            try:
                num = int(num)
                if num > MAX_REQUIRED_NUM:
                    num = MAX_REQUIRED_NUM
            except:
                num = DEFAULT_NUM
        else:
            num = DEFAULT_NUM

        v_num = request.GET.get('v_num',None)
        if v_num:
            try:
                v_num = int(v_num)
                valid_ip = valid_ip.filter(Validated_time__gte=v_num)
            except:
                pass
        else:
            pass

        type = request.GET.get('type',None)
        if type and type.upper() in ['O','G','T']:
            valid_ip = valid_ip.filter(type__iexact=type)
        else:
            pass

        location = request.GET.get('loc',None)
        if location:
            valid_ip = valid_ip.filter(district__contains = location)

        head = request.GET.get('head',None)
        if head and head.lower() == 'https':
            head = 'https'

        else:
            head = 'http'

        valid_ip = valid_ip.filter(head__contains=head)

        data = {}
        ip_list = []
        count = 0

        for i in valid_ip:
            if count == num:
                break
            if not i.ip:
                continue
            proxy = {}

            proxy[head] = i.ip + ':' + i.port
            proxy['最后验证时间'] = i.last_modified_time.strftime('%Y-%m-%d %I:%M:%S')
            proxy['验证次数'] = i.Validated_time
            if i.type == 'T':
                proxy['类型'] = '透明'
            else:
                proxy['类型'] = '高匿'

            count += 1
            ip_list.append(proxy)

        data['proxies'] = ip_list
        data['code'] = 1

        return JsonResponse(data)

# ================api 说明=============================================

def api_ins(request):

    return render(request,'myproxy/api_instruction.html')


# ================ 防止请求过快 ====================================

def judge_request(request):

    addr = request.META.get('REMOTE_ADDR')
    query = IpAddr.objects.filter(addr=addr)
    if query:

        addrins = query[0]

        if addrins.limit == 'T':
            return False
        if addrins.limit_count > 5:
            addrins.limit = 'T'

        addrins.req_count += 1
        # diff_timedelta = datetime.now(timezone.utc) - addrins.last_modified_time
        diff_timedelta = datetime.now() - addrins.last_modified_time
        # print(diff_timedelta)
        diff = diff_timedelta.seconds
        # print(diff)

        if diff < 3:
            addrins.limit_count += 1
            return False

        addrins.save()


    else:
        IpAddr.objects.create(
            addr = addr,
            req_count = 1,
        )

    return True
