from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^/buy$', views.index),
    url(r'^amadon$', views.index),
    url(r'^$', views.index)
]