from django.shortcuts import render,redirect
from adminapp.models import Student,Attendance
from teacherapp.models import StudyMaterial
from django.core.files.storage import FileSystemStorage

# Create your views here.

def studenthome(req):
    try:
        if req.session['studentid']!=None:
           studentid=req.session['studentid']
           student=Student.objects.get(emailaddress=studentid)
           
           return render(req,'studenthome.html',{'student':student})
    except KeyError:
        return redirect('login')
def stuattend(req):
    try:
        if req.session['studentid']!=None:
           studentid=req.session['studentid']
           student=Student.objects.get(emailaddress=studentid)
           att=Attendance.objects.filter(sid=student.id)
           return render(req,'stuattend.html',{'student':student,'att':att})
    except KeyError:
        return redirect('login')
def stuslm(req):
    try:
        if req.session['studentid']!=None:
           studentid=req.session['studentid']
           student=Student.objects.get(emailaddress=studentid)
           slm=StudyMaterial.objects.filter(tclass=student.sclass)
           return render(req,'stuslm.html',{'student':student,'slm':slm})
    except KeyError:
        return redirect('login')
    
def studentlogout(req):
    try:
        if req.session['studentid']!=None:
          del req.session['studentid']
          return redirect('login')
    except KeyError:
        return redirect('login')
     
def stchangepass(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            if req.method=="POST":
                oldpassword=req.POST['oldpassword']
                newpassword=req.POST['newpassword']
                cnfpassword=req.POST['cnfpassword']
                if newpassword!=cnfpassword:
                    msg="Please confirm same password..."
                    return render(req,'stchangepass.html',{'msg':msg})
                elif student.password!=oldpassword:
                    msg="Please enter old password..."
                    return render(req,'stchangepass.html',{'msg':msg})
                elif newpassword==oldpassword:
                    msg="New Password can't be the old one..."
                    return render(req,'stchangepass.html',{'msg':msg})
                elif student.password==oldpassword:
                    Student.objects.filter(emailaddress=studentid).update(password=newpassword)
                    return redirect('login')
            return render(req,'stchangepass.html',{'student':student})
    except KeyError:
        return redirect('login')
def studentprofile(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                address=req.POST['address']
                feepaid=req.POST['feepaid']
                duefees=req.POST['duefees']
               
                Student.objects.filter(emailaddress=studentid).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,address=address,feepaid=feepaid,duefees=duefees)
              
                return redirect ('studentapp:studentprofile')

            return render(req,'studentprofile.html',{'student':student})
    except KeyError:
        return redirect('login')
# upload pic

def uploadpic (req):
    if req.method=="POST":
        studentid=req.session['studentid']
        student=Student.objects.get(emailaddress=studentid)
        pic=req.FILES['pic']
        fs=FileSystemStorage()
        filename=fs.save(pic.name,pic)
        student.pic=filename
        student.save()
        return redirect ('studentapp:studentprofile')

