#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms

def test(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test.html', context)
