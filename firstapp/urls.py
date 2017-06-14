from django.conf.urls import url

from firstapp import views

urlpatterns = [
    url(r'^index.html', views.index),
    url(r'^suning', views.suning)
]
