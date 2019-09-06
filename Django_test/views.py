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


# 重定向
def index_one(request):
    #return HttpResponse('index one')
    # url = reverse('i2') # 通过命名空间转换地址
    #return HttpResponseRedirect(url)
    return redirect('i2')   # 这里可以传命名空间 或者 url


def index_two(request):
    return HttpResponse('index two')



# 重写内置视图
def page_500(request):
    return HttpResponse('服务器正忙')