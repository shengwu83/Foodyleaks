from django.shortcuts import render
from django.shortcuts import render_to_response
from models import PesticideVegatable,News
import json

# Create your views here.
def news_detail(resquest,news_id):
    n = News.objects.filter(id=news_id)[0]
    print n.title
    return render_to_response('newsdetail.html',{"title":n.title,"n":n})

def news(resquest):
    bign = News.objects.all().order_by('-timestamp')[0]
    ns = News.objects.all().order_by('-timestamp')[1:11]
    
    return render_to_response("news.html", {"title":"News","ns":ns,"bign":bign})

def trend(resquest):
    print 'trend'
    return render_to_response("trend.html", {"title":"FoodyLeaks"})