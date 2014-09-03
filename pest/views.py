# -*- coding: UTF-8 -*-    
from django.shortcuts import render_to_response
from django.template import Context
from models import Violation


# Create your views here.
def pest(resquest):
    vs = Violation.objects.filter(category="廣告不實",date__contains='102').order_by('-date').reverse()[0:10]
    return render_to_response('pest.html',{"title":"Pesticide","vs":vs})


def index(resquest):
    #pvs = PesticideVegatable.objects.filter(month="1")
    return render_to_response("index.html", {"title":"FoodyLeaks"})
