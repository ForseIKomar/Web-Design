# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpResponce

class AboutView(TemplateView):
    template_name = "about.html"

def ParseParam(query):
    return ''.join('<h1>{} = {}</h1>'.format(i, query[i]) for i in query)
 
def GetPost(request):
    print('Get and Post')
    printing_string = ParseParam(request.GET) + ParseParam(request.POST) + parseParams(request.FILES)
    return HttpResponce(printing_string)


