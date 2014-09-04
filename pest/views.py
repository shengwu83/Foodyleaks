# -*- coding: UTF-8 -*-    
from django.shortcuts import render_to_response
from django.template import Context
from models import Violation
import json
import os

# Create your views here.
def pest(resquest):
    cate = resquest.GET.get('cate')
    date = resquest.GET.get('date')
    cate0 = cate
    if (cate is None):
        cate = '農藥超標'
        date = ''
        vs = Violation.objects.filter(category__contains=cate,date__contains=date).order_by('-date').reverse()[0:10]   
    else:
        cate = cate.encode('utf-8')
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
        vs = Violation.objects.filter(category__contains=cate,date__contains=date).order_by('-date').reverse()[0:10]
    
    #data = data.decode('utf-8')
    return render_to_response('pest.html',{"title":"Pesticide","vs":vs, "cate": cate0})

def index(resquest):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    json_data = open(BASE_DIR+'/static/index.json')
    data = json.load(json_data)
    json_data.close()
    return render_to_response("index.html", {"title":"FoodyLeaks","data" : data})
