from django.conf.urls import url

from . import views as pages_v

urlpatterns = [
    url(r'^index/$', pages_v.index),
]
