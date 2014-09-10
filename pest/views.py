# -*- coding: UTF-8 -*-    
from django.shortcuts import render_to_response
from django.template import Context
from models import Violation
import json
import os
import urllib

from django.views.generic import ListView

class CarListView(ListView):
    model = Violation      # shorthand for setting queryset = models.Car.objects.all()
    template_name = 'pest.html'  # optional (the default is app_name/modelNameInLowerCase_list.html; which will look into your templates folder for that path and file)
    context_object_name = "violation_list"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 10  #and that's it !!

def pest(request):
    cate = request.GET.get('cate','1')
    date = request.GET.get('date','103')
    page = request.GET.get('page',1)
    key = request.GET.get('key','')
    
    
    params = request.GET.urlencode()
    
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
    print date
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
