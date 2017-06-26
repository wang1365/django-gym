from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import requests
from django.core.cache import cache
from django.conf import settings
from django.http import HttpRequest
from firstapp.models import User, Country


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


# Sample: https://127.0.0.1:8000/firstapp/register?user=wangxiaochuan&age=30&country=1&password=12345
def register(req):
    if settings.DEBUG:
        name, age, country, password = req.GET['user'], int(req.GET.get('age', -1)), int(req.GET['country']), req.GET[
            'password']
        print name, age, country, password
        user = User(name=name, age=age, country=Country.objects.get(id=country))
        user.save()
    else:
        raise NotImplementedError("Post register not implemented for release env")
    return HttpResponse('Register success')


# Sample: https://127.0.0.1:8000/firstapp/user?userid=1
def get_user(req):
    user_id = int(req.GET.get('userid'))
    key = 'firstapp.user.%d' % user_id
    user = cache.get(key)
    if not user:
        print 'Key[%s] doesnot exist in redis, read it from DB, and add to redis'%key
        user = User.objects.get(id=user_id)
        print 'user:', user
        cache.set(key, user)

    import json

    return HttpResponse(json.dumps(user))
