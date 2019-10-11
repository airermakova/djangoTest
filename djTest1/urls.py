from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^count_fact/$',views.HomePageView.count_fact,name='count_fact'),
    url(r'^getAA/$',views.HomePageView.getAA,name='getAA')
]