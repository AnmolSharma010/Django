from django import urls
from django.urls import path
from .views import homePageView

urlspatterns =[
    path('',homePageView,name='home')
]
