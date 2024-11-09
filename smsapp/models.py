from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)

#admin login details
class AdminLogin(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

