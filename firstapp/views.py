from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import requests


# Create your views here.

def index(req):
    return HttpResponse("<h1>This is firstapp of django<h1>");


def suning(req):
    if req.method not in ('GET',):
        raise HttpResponseNotAllowed()

    url_suning = r'http://www.suning.com/'
    res = requests.get(url_suning)
    if res.ok:
        return HttpResponse(res.content)
