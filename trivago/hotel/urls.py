
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    # url(r'^gwalior/',views.IndexView.as_view()),
    url(r'^search/',views.search,name='search'),
]
