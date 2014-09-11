# -*- coding: UTF-8 -*-    
from django.shortcuts import render_to_response
from django.template import Context
from models import Violation
import json
import os
import urllib

def pest(request):
    cate = request.GET.get('cate','1')
    date = request.GET.get('date','103')
    page = request.GET.get('page',1)
    key = request.GET.get('key','')
    params = request.GET.copy()
    if params.has_key('page'):
        del params['page']
    
    params = params.urlencode()
    print params
    
    current = ''
    cate_num = cate
    if page is not None:
        page = int(page) - 1
        first = page * 10 
        last = first + 11
    else:
        page = 1
        first = 0
        last = 11
    
    cate = cate.encode('utf-8')
    date = date.encode('utf-8')
    key = key.encode('utf-8')
    if cate == '1':
        cate = '農藥超標'
    elif cate == '2':
        cate = '不符使用'
    elif cate == '3':
        cate = '廣告不實'
    else:
        cate = ''
    if type(date) == None:
        date = 103
    if type(date) == None:
        key = ''
    vs_all = Violation.objects.filter(category__contains=cate,date__contains=date,product__contains=key).order_by('-timestamp')
    pages = int(vs_all.count()/10) + 2
    if pages > 11:
        pages = 11
    vs = vs_all[first:last]
    #data = data.decode('utf-8')
    return render_to_response('pest.html',{"title":"Pesticide",
                                           "vs":vs,
                                           "cate": cate_num ,
                                           'pages':range(1,pages),
                                           "page": page+1,
                                           "params":params})

def index(resquest):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    json_data = open(BASE_DIR+'/static/index.json')
    data = json.load(json_data)
    json_data.close()
    return render_to_response("index.html", {"title":"FoodyLeaks","data" : data})
