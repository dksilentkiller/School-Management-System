from django.urls import path
from . import views

# Teacher app urls
urlpatterns = [
    path('teacherapp/',views.teacherhome,name='teacherhome'),
    path('teacherprofile/',views.teacherprofile,name='teacherprofile'),
    path('uplaodpic/',views.uploadpic,name='uploadpic'),
    path('tchangepass/',views.tchangepass,name='tchangepass'),
    path('teacherlogout/',views.teacherlogout,name='teacherlogout'),    
    path('addattend/',views.addattend,name='addattend'),
    path('viewattend/',views.viewattend,name='viewattend'),
    path('addslm/',views.addslm,name='addslm'),
     path('viewslm/',views.viewslm,name='viewslm'),


]
