# -*- coding: UTF-8 -*-    
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import PesticideVegatable,News
import json

# Create your views here.
def news_detail(resquest,news_id):
    n = News.objects.filter(id=news_id)[0]
    return render_to_response('newsdetail.html',{"title":n.title,"n":n})

def news(resquest):
    page = resquest.GET.get('page')
    
    if page is not None:
        page = int(page) - 1
        first = page * 10 + 1
        last = first + 11
    else:
        page = 0
        first = 1
        last = 11
    ns_all = News.objects.all().order_by('-timestamp')
    pages = ns_all.count()
    
    bign = News.objects.all().order_by('-timestamp')[first]
    ns = News.objects.all().order_by('-timestamp')[first:last]
    
    return render_to_response("news.html", {"title":"News",
                                            "ns":ns,"bign":bign,
                                            "pages":range(1,11),
                                            "page": page+1})

def trend(resquest):
    print 'trend'
    return render_to_response("trend.html", {"title":"FoodyLeaks"})