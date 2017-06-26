from django.conf.urls import url

from . import views
from django.conf.urls import include
from rest_framework import routers
from .viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^index.html', views.index),
    url(r'^suning', views.suning),
    url(r'^register$', views.register),
    url(r'^user$',views.get_user)
]
