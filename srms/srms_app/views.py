from django.shortcuts import render

import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, 'index.html')


def student_login(request):
    if request.method == 'POST':
        a = stud_login(request.POST)
        if a.is_valid():
            regnum = a.cleaned_data['regno']
            ps = a.cleaned_data['psw']
            b = studentregister_model.objects.all()
            for i in b:
                if i.register_num == regnum and i.password==ps:
                    request.session['id'] = i.id
                    return redirect(student_view_page)
            else:
                 return HttpResponse("Login failed")

    return render(request, 'student login.html')


from django.contrib.auth import authenticate


def adminlogin(request):
    if request.method == 'POST':
        a = adminform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']
            ps = a.cleaned_data['password']
            user = authenticate(request, username=us, password=ps)
            if user is not None:
                return redirect(adminview)
            else:
                return HttpResponse("Login failed")

    return render(request, 'admin login.html')

def adminview(request):
    if request.method=='POST':
        a=adminsort(request.POST)
        if a.is_valid():
            dpt=a.cleaned_data['department1']
            b=studentregister_model.objects.all()
            for i in b:
                if i.department==dpt:
                    request.session['id'] = i.id
                    return render(request,'student sort.html',{'b':b})
            else:
                return HttpResponse("Login failed")
    return render(request,'admin view.html')

def deletedata(request,id):
    a=studentregister_model.objects.get(id=id)
    a.delete()
    return redirect(adminview)

def editdata(request,id):
    b=studentregister_model.objects.get(id=id)
    if request.method=='POST':
        b.firstname=request.POST.get('firstname')
        b.lastname=request.POST.get('lastname')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phone')
        b.department=request.POST.get('department')
        b.save()
        return redirect(adminview)
    return render(request,'update student details.html',{'b':b})

def Student_Register(request):
    if request.method == 'POST':
        a = studentregister(request.POST)
        if a.is_valid():
            fname = a.cleaned_data['firstname']
            lname = a.cleaned_data['lastname']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            dep = a.cleaned_data['department']
            reg = ("R191" + str(ph))
            pin = a.cleaned_data['password']
            repin = a.cleaned_data['confirmpassword']
            if pin == repin:
                b = studentregister_model(firstname=fname, lastname=lname, email=em, phone=ph, department=dep,
                                          register_num=reg,password=pin)
                b.save()
                # subject = "Your account has been created"
                # message = f"Your Register Number is{reg}"
                # email_from = "skyviewwwww@gmail.com"
                # email_to = em
                # send_mail(subject, message, email_from, [email_to])
                return HttpResponse("Success")
            else:
                return HttpResponse("Password error")
        else:
            return HttpResponse("Registration failed")
    return render(request, 'student register.html')


def addresult(request,id):
    a=studentregister_model.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname = request.POST.get('lastname')
        a.register_num = request.POST.get('register_num')
    return render(request,'add result.html',{'a':a})

def firstsem(request,id):
    a=studentregister_model.objects.get(id=id)
    if request.method == 'POST':
        x = first_sem(request.POST)
        if x.is_valid():
            # id3 = request.session['id']
            id3=a.id
            ar = x.cleaned_data['arabic']
            en = x.cleaned_data['english']
            c = x.cleaned_data['C']
            de = x.cleaned_data['DE']
            dm = x.cleaned_data['DM']
            c_lab = x.cleaned_data['c_programming_Lab']
            de_lab = x.cleaned_data['DE_Lab']
            env = x.cleaned_data['environment']
            b = first_sem_model1(id2=id3,arabic=ar, english=en, C=c, DE=de, DM=dm, c_programming_Lab=c_lab, DE_Lab=de_lab,
                                environment=env)
            b.save()
            return redirect(marlistsuccess)
        else:
            return HttpResponse("Mark Uploaded Failed")
    return render(request,'first semester.html',{'a':a})

def secondsem(request,id):
    a = studentregister_model.objects.get(id=id)
    if request.method == 'POST':
        x=second_sem(request.POST)
        if x.is_valid():
            # id3 = request.session['id']
            id3=a.id
            ar=x.cleaned_data['arabic']
            en=x.cleaned_data['english']
            ds=x.cleaned_data['DS']
            dbms=x.cleaned_data['DBMS']
            nsm=x.cleaned_data['NSM']
            ds_lab=x.cleaned_data['DS_Lab']
            dbms_lab=x.cleaned_data['DBMS_Lab']
            ichr=x.cleaned_data['ICHR']
            b=second_sem_model(id2=id3,arabic=ar,english=en,DS=ds,DBMS=dbms,DS_Lab=ds_lab,DBMS_Lab=dbms_lab,ICHR=ichr,NSM=nsm)
            b.save()
            return redirect(marlistsuccess)
    return render(request,'second semester.html',{'a':a})

def thirdsem(request,id):
    a=studentregister_model.objects.get(id=id)
    if request.method=='POST':
        x=third_sem(request.POST)
        if x.is_valid():
            # id3 = request.session['id']
            id3=a.id
            ar=x.cleaned_data['arabic']
            en=x.cleaned_data['english']
            cpp=x.cleaned_data['Cpp']
            accounting=x.cleaned_data['Accounting']
            operatingsystem=x.cleaned_data['OperatingSystem']
            cpplab=x.cleaned_data['Cpp_Lab']
            acc_lab=x.cleaned_data['Accounting_Lab']
            cds=x.cleaned_data['CDS']
            b=third_sem_model(id2=id3,arabic=ar,english=en,Cpp=cpp,Accounting=accounting,Cpp_Lab=cpplab,Accounting_Lab=acc_lab,CDS=cds,OperatingSystem=operatingsystem)
            b.save()
            return redirect(marlistsuccess)

    return render(request,'third semester.html',{'a':a})

def fourthsem(request,id):
    a = studentregister_model.objects.get(id=id)
    if request.method == 'POST':
        a.firstname = request.POST.get('firstname')
        a.lastname = request.POST.get('lastname')
        a.register_num = request.POST.get('register_num')
        x=fourth_sem(request.POST)
        if x.is_valid():
            # id3 = request.session['id']
            id3=a.id
            ar=x.cleaned_data['arabic']
            en=x.cleaned_data['english']
            vp=x.cleaned_data['Vprogramming']
            usp=x.cleaned_data['USprogramming']
            Or=x.cleaned_data['oR']
            vpl=x.cleaned_data['Vp_Lab']
            unix_lab=x.cleaned_data['UNIX_Lab']
            pd=x.cleaned_data['PD']
            b=fourth_sem_model(id2=id3,arabic=ar,english=en,Vprogramming=vp,USprogramming=usp,oR=Or,Vp_Lab=vpl,UNIX_Lab=unix_lab,PD=pd)
            b.save()
            return redirect(marlistsuccess)

    return render(request,'fourth semester.html',{'a':a})

def fifthsem(request,id):
    a = studentregister_model.objects.get(id=id)
    if request.method == 'POST':
        a.firstname = request.POST.get('firstname')
        a.lastname = request.POST.get('lastname')
        a.register_num = request.POST.get('register_num')
        x = fifth_sem(request.POST)
        if x.is_valid():
            # id3 = request.session['id']
            id3=a.id
            dcn=x.cleaned_data['DCN']
            se=x.cleaned_data['SE']
            jp=x.cleaned_data['JP']
            mp=x.cleaned_data['MP']
            Pro=x.cleaned_data['Project']
            bf=x.cleaned_data['BF']
            ca=x.cleaned_data['CA']
            b=fifth_sem_model(id2=id3,DCN=dcn,SE=se,JP=jp,MP=mp,Project=Pro,BF=bf,CA=ca)
            b.save()
            return redirect(marlistsuccess)
    return render(request,'fifth semester.html',{'a':a})

def sixthsem(request,id):
    a = studentregister_model.objects.get(id=id)
    if request.method == 'POST':
        x = sixth_sem(request.POST)
        if x.is_valid():
            # id3 = request.session['id']
            id3=a.id
            toc=x.cleaned_data['TOC']
            sp=x.cleaned_data['SP']
            cns=x.cleaned_data['CNS']
            wp=x.cleaned_data['WP']
            wpl=x.cleaned_data['WPL']
            Pro=x.cleaned_data['Project']
            cait=x.cleaned_data['CAIT']
            b=sixth_sem_model(id2=id3,TOC=toc,SP=sp,CNS=cns,WP=wp,WPL=wpl,Project=Pro,CAIT=cait)
            b.save()
            return redirect(marlistsuccess)
    return render(request,'sixth semester.html',{'a':a})


def marlistsuccess(request):
    return render(request,'marklist uploaded success.html')


def student_view_page(request):
    try:
        id1=request.session['id']
        a=studentregister_model.objects.get(id=id1)
        # id2=request.session['id']
        return render(request,'student viewpage.html',{'a':a})
    except:
        return redirect(student_login)

from .models import studentregister_model,sixth_sem_model
def sixthsem_markcard(request,id):
    id1 = request.session['id']
    b = sixth_sem_model.objects.get(id2=id1)
    a=studentregister_model.objects.get(id=id)
    context={
        'a':a,
        'b':b
    }


    return render(request,'sixth semester markcard.html',context)

def fifthsem_markcard(request,id):
    id1 = request.session['id']
    b = fifth_sem_model.objects.get(id2=id1)
    a = studentregister_model.objects.get(id=id)
    context = {
        'a': a,
        'b': b
    }
    return render(request,'fifth semester markcard.html',context)


def fourthsem_markcard(request,id):
    id1 = request.session['id']
    b = fourth_sem_model.objects.get(id2=id1)
    a = studentregister_model.objects.get(id=id)
    context = {
        'a': a,
        'b': b
    }
    return render(request,'fourth semester markcard.html',context)

def thirdsem_makcard(request,id):
    id1 = request.session['id']
    b = third_sem_model.objects.get(id2=id1)
    a = studentregister_model.objects.get(id=id)
    context = {
        'a': a,
        'b': b
    }
    return render(request,'third semester markcard.html',context)


def secondsem_markcard(request,id):

    id1 = request.session['id']
    b = second_sem_model.objects.get(id2=id1)
    a = studentregister_model.objects.get(id=id)
    context = {
        'a': a,
        'b': b
    }
    return render(request,'second semester markcard.html',context)


def firstsem_markcard(request,id):
    id1 = request.session['id']
    b = first_sem_model1.objects.get(id2=id1)
    a = studentregister_model.objects.get(id=id)
    context = {
        'a': a,
        'b': b
    }
    return render(request,'first semester markcard.html',context)

def show_result6(request):

    # a=sixth_sem_model.objects.get(id=id)

    return render(request,'show_result.html')


def courses(request):
    return render(request,'courses.html')

def contact(request):
    return render(request,'contact us.html')