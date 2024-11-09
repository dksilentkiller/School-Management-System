from django.urls import path
from.import views

#student app urls
urlpatterns=[
    path('studentapp/',views.studenthome,name='studenthome'),
    path('stuattend/',views.stuattend,name='stuattend'),
    path('stuslm/',views.stuslm,name='stuslm'),
    path('studentprofile/',views.studentprofile,name='studentprofile'),
    path('studentlogout/',views.studentlogout,name='studentlogout'),
  
    path('uplaodpic/',views.uploadpic,name='uploadpic'),
    path('stchangepass/',views.stchangepass,name='stchangepass'),

]