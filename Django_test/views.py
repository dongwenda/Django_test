from datetime import datetime
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import loader
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect, reverse




def now_time(request):
    '''返回html模版'''
    now = datetime.now()
    html = '''
    <html>
        <head>
            <style type="text/css">
            body{{color: red;}}
            </style>
        </head>
        <>body>'now: {0} '</body>
    </html>
    '''.format(now)
    return HttpResponse(html)



def article(request, year):
    '''获取get的参数'''
    month = request.GET.get('month', 11)
    day = request.GET.get('day', 11)
    return HttpResponse(f'year: {year}, month: {month}, day: {day}')


def now_use_file(request):
    '''返回html文件'''
    html = ''

    now = datetime.now()
    # 方法1
    # file_name = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    # with open(file_name) as f:
    #     html = f.read()
    # html = html.replace('{{now}}', now.strftime('%Y-%M-%D'))
    # return HttpResponse(html.template.source)

    # 方法2
    # templ = loader.get_template('index.html')
    # html = templ.render({
    #     'now': now
    # })
    # return HttpResponse(html)

    # 方法3
    # return render(request, 'index.html', {
    #     'now': now
    # })

    # 方法4
    return render_to_response('index.html', {
        'now': now
    })


def print_json(request):
    '''响应json对象'''
    user_info = {
        "username": 'apple',
        'age': 18
    }
    # import json
    # user_info = json.dumps(user_info)
    # return HttpResponse(user_info, content_type='application/json')

    from django.http import JsonResponse
    return JsonResponse(user_info)


def print_request(request):
    '''请求头信息'''
    print(request)
    print(request.META['REMOTE_ADDR'])  # 获取访问的ip
    print(request.META['HTTP_USER_AGENT'])  # UA
    print('----------------------')
    print(dir(request))
    return HttpResponse()


def print_resp(request):
    '''响应对象'''
    resp = HttpResponse('响应对象', status=404) # 设置http响应码
    resp.status_code = 204 # 设置http响应码
    print(resp.status_code)
    return resp


def print_image(request):
    '''打印图片'''
    from django.http import FileResponse
    file_path = os.path.join(settings.BASE_DIR, 'medias/images/aapp.png')
    f = open(file_path, 'rb')
    return FileResponse(f, content_type='image/png')

def print_xls(request):
    '''下载xls'''
    from django.http import FileResponse
    file_path = os.path.join(settings.BASE_DIR, 'medias/test.xls')
    f = open(file_path, 'rb')
    return FileResponse(f, content_type='application/vnd.ms-excel')


from django.views.generic import TemplateView
class ShowClassView(TemplateView):
    """class 视图"""
    template_name = 'show_class.html'


# 重定向
def index_one(request):
    #return HttpResponse('index one')
    # url = reverse('i2') # 通过命名空间转换地址
    #return HttpResponseRedirect(url)
    return redirect('i2')   # 这里可以传命名空间 或者 url


def index_two(request):
    return HttpResponse('index two')

def templ_show(request):
    # 模版引擎选择
    return render_to_response('detail.html')

# 重写内置视图
def page_500(request):
    return HttpResponse('服务器正忙')