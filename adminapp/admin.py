from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Classes)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Notification)

