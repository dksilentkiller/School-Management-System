from django.shortcuts import render,redirect
from smsapp.models import Enquiry
from django.utils import timezone
import datetime
from . models import *
from django.views.decorators.cache import cache_control

import datetime

# Create your views here.
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def adminhome(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            stu_count=Student.objects.all().count()
            t_count=Teacher.objects.all().count()
            subcount=Subject.objects.all().count()
            clcount=Classes.objects.all().count()
            ps=Attendance.objects.filter(status="P",created_date=datetime.date.today()).count()
            abs=Attendance.objects.filter(status="A",created_date=datetime.date.today()).count()
            noticount=Notification.objects.all().count()
            enqcount=Enquiry.objects.all().count()
            context={'adminid':adminid,'stu_count':stu_count,'t_count':t_count,'subcount':subcount,'clcount':clcount,'ps':ps,'abs':abs ,'noticount':noticount,'enqcount':enqcount}
            return render(req,'adminhome.html',context)
    except KeyError:
        return redirect('login')  

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewenquiry(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            enq=Enquiry.objects.all()
            return render(req,'viewenquiry.html',{'adminid':adminid,'enq':enq})
    except KeyError:
        return redirect('login')  

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def addclass(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            if req.method=="POST":
                class_name=req.POST['class_name']
                seats=req.POST['seats']
                roomno=req.POST['roomno']
                created_date=timezone.now()
                

                cl=Classes(class_name=class_name,seats=seats,roomno=roomno,created_date=created_date)
                cl.save()
                return redirect('adminapp:viewclass')
            return render(req,'addclass.html',{'adminid':adminid})
    except KeyError:
        return redirect('login')  

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewclass(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            return render(req,'viewclass.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')  

@cache_control(no_store=True,no_cache=True,must_revalidate=True)                         
def adminlogout(req):
    try:
        if req.session['adminid']!=None:
            del req.session['adminid']
            return redirect('login')
    except KeyError:
        return redirect('login')        


def addsubject(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method=="POST":
                subject_name=req.POST['subject_name']
                sclass=req.POST['sclass']
                book=req.POST['book']
                steacher=req.POST['steacher']
                created_date=timezone.now()
                
                sub=Subject(subject_name=subject_name,sclass=sclass,book=book,steacher=steacher,created_date=created_date)
                sub.save()
                return redirect('adminapp:viewsubject')
            return render(req,'addsubject.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')  

def viewsubject(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            sub=Subject.objects.all()
            return render(req,'viewsubject.html',{'adminid':adminid,'sub':sub})
    except KeyError:
        return redirect('login')  
@cache_control(no_store=True,no_cache=True,must_revalidate=True) 
def editsub(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            sub=Subject.objects.get(sid=id)
            cl=Classes.objects.all()
            if req.method=="POST":
                sid=req.POST["sid"]
                subject_name=req.POST["subject_name"]
                sclass=req.POST["sclass"]
                book=req.POST["book"]
                steacher=req.POST["steacher"]
                Subject.objects.filter(sid=sid).update(subject_name=subject_name,sclass=sclass,book=book,steacher=steacher)
                return redirect('adminapp:viewsubject')
            return render(req,'editsubject.html',{'adminid':adminid,'sub':sub,'cl':cl})
    except KeyError:
        return redirect('login') 


def delenq(req,id):
    try:
        if req.session!=None:
            Enquiry.objects.get(id=id).delete()
            return redirect('adminapp:viewenquiry')    
    except KeyError:
        return redirect('login')

        

def editclass(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.get(cid=id)
            if req.method == 'POST':
                class_name=req.POST['class_name']
                seats=req.POST['seats']
                roomno=req.POST['roomno']
                Classes.objects.filter(cid=id).update(class_name=class_name,seats=seats,roomno=roomno)
                return redirect('adminapp:viewclass')
            return render(req,'editclass.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')          


def addteacher(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                tclass=req.POST['tclass']
                address=req.POST['address']
                salary=req.POST['salary']
                qualification=req.POST['qualification']
                created_date=timezone.now()
                tech=Teacher(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,tclass=tclass,address=address,salary=salary,qualification=qualification,created_date=created_date,password="12345")
                tech.save()
                return redirect('adminapp:viewteacher')
            return render(req,'addteacher.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')   


def viewteacher(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            tech=Teacher.objects.all()
            return render(req,'viewteacher.html',{'adminid':adminid,'tech':tech})
    except KeyError:
        return redirect('login') 

def delclass(req,cid):
    try:
        if req.session!=None:
            Classes.objects.get(cid=cid).delete()
            return redirect('adminapp:viewclass')    
    except KeyError:
        return redirect('login')         

def delsubject(req,sid):
    try:
        if req.session!=None:
            Subject.objects.get(sid=sid).delete()
            return redirect('adminapp:viewsubject')    
    except KeyError:
        return redirect('login')    
       

def delteacher(req,id):
    try:
        if req.session!=None:
            Teacher.objects.get(id=id).delete()
            return redirect('adminapp:viewteacher')    
    except KeyError:
        return redirect('login')    
            
def editteacher(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            tech=Teacher.objects.get(id=id)
            cl=Classes.objects.all()
            if req.method == 'POST':
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                tclass=req.POST['tclass']
                address=req.POST['address']
                salary=req.POST['salary']
                qualification=req.POST['qualification']
                Teacher.objects.filter(id=id).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,tclass=tclass,address=address,salary=salary,qualification=qualification)
                return redirect('adminapp:viewteacher')
            return render(req,'editteacher.html',{'adminid':adminid,'tech':tech,'cl':cl})
    except KeyError:
        return redirect('login') 

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def addstudent(req):
    try:

        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method=='POST':
                rollno=req.POST['rollno']
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress =req.POST['emailaddress']
                sclass=req.POST['sclass']
                address=req.POST['address']
                feepaid=req.POST['feepaid']
                duefees=req.POST['duefees']
                password='12345'
                      
                created_date=timezone.now()
                stu=Student.objects.filter(emailaddress=emailaddress).first()
                if stu is not None:
                    return render(req,'addstudent.html',{'adminid':adminid,'cl':cl,'msg':'This emailaddress is already taken'})
                
                else:
                    st=Student( rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,sclass=sclass,address=address,feepaid=feepaid,duefees=duefees, password= password,created_date=created_date)
                    st.save()
                    return redirect('adminapp:viewstudent')                  

                
            
            return render(req,'addstudent.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login') 
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewstudent(req):
    try:

        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            st=Student.objects.all()
            return render(req,'viewstudent.html',{'adminid':adminid,'st':st})
    except KeyError:
        return redirect('login') 
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def delst(req,id):
    try:
        if req.session['adminid']!=None:
            st=Student.objects.get(rollno=id)
            st.delete()
            return redirect('adminapp:viewstudent')
    except KeyError:
        return redirect('login') 
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def editst(req,id):
    try:
       
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            st=Student.objects.get(rollno=id)
            cl=Classes.objects.all()
            if req.method=='POST':
                rollno=req.POST['rollno']
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                sclass=req.POST['sclass']
                address=req.POST['address']
                feepaid=req.POST['feepaid']
                duefees=req.POST['duefees']
                password='12345'
                      
                
                Student.objects.filter ( rollno=rollno).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,sclass=sclass,address=address,feepaid=feepaid,duefees=duefees, password= password)
                return redirect('adminapp:viewstudent')
            return render(req,'editstudent.html',{'adminid':adminid,'st':st,'cl':cl})
    except KeyError:
        return redirect('login') 


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def addnoti(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']

            if req.method=="POST":
                text=req.POST['text']
                doc=req.FILES['doc']
                created_date=datetime.date.today()
                noti=Notification(text=text,doc=doc,created_date=created_date)
                noti.save()
                return redirect('adminapp:viewnoti')
            return render(req,'addnoti.html',{'adminid':adminid})
    except KeyError:
        return redirect('login') 

@cache_control(no_store=True,no_cache=True,must_revalidate=True)    
def viewnoti(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            noti=Notification.objects.all()        
            return render(req,'viewnoti.html',{'adminid':adminid,'noti':noti})
    except KeyError:
        return redirect('login') 
@cache_control(no_store=True,no_cache=True,must_revalidate=True)  
def delnoti(req,id):
    try:
        if req.session['adminid']!=None:
            noti=Notification.objects.get(nid=id)
            noti.delete()
            return redirect('adminapp:viewnoti')
    except KeyError:
        return redirect('login') 