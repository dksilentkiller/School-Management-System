from django.urls import path
from . views import *

urlpatterns=[
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('aboutus/',aboutus,name='aboutus'),
    path('aboutfounder/',aboutfounder,name='aboutfounder'),
    path('aboutchairman/',aboutchairman,name='aboutchairman'),
    path('aboutprinciple/',aboutprinciple,name='aboutprinciple'),
    path('aboutmanagement/',aboutmanagement,name='aboutmanagement'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('news/',news,name='news'),
    path('logcode/',logcode,name='logcode'),
    path('academic/',academic,name='academic'),
    path('transport/',transport,name='transport'),
    path('medical/',medical,name='medical'),
    path('smartclass/',smartclass,name='smartclass'),
]