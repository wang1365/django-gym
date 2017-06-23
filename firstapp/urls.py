from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index.html', views.index),
    url(r'^suning', views.suning),
    url(r'^register$', views.register),
    url(r'^user$',views.get_user)
]
