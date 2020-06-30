from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .Auth import Authetic
from django.db import IntegrityError
from .models import appusers
from projects.models import customerinfo, developerinfo
from django.template.response import TemplateResponse

from django.contrib import messages


# Create your views here.
#should add if user already signed in refresh session
def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        given_password = request.POST.get('pass')
        result = appusers.objects.filter(username=username)
        password = ''
        for index in result:
            password = index.password
        authobject = Authetic(password)
        decrypt_password = authobject.decrypt(password)
        if given_password == decrypt_password:
            for index in result:
                idiotita = index.idiotita
            request.session['username'] = username
            request.session['idiotita'] = idiotita
            #test
            #if request.session:
            #   return HttpResponse( request.session['username'])
            return redirect('/')

        else:
            arguments = {}
            arguments['mnm'] = "! Wrong Password or Username !"
            return TemplateResponse(request, 'auth/LoginForm.html', arguments)
    else:
        return render(request, 'auth/LoginForm.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        location = request.POST.get('location')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        password = request.POST.get('pass')
        idiotita = request.POST.get('member_level')
        Password = str(password)
        authobject = Authetic(Password)
        try:
            if idiotita == "developer"  :
                newuser = appusers.objects.create(username=username,fullname=fullname,location=location,email=email,birthday=birthday,password=str(authobject.encrypt()),idiotita=idiotita)
                userinfo = developerinfo.objects.create(
                    username=username,
                    location="location",
                    language="language",
                    github="github",
                    cv="cv",
                    profile_pic="profile_pic",
                    )
            else:
                newuser = appusers.objects.create(username=username,fullname=fullname,location=location,email=email,birthday=birthday,password=str(authobject.encrypt()),idiotita=idiotita,rating="-24")
                userinfo = customerinfo.objects.create(
                    username=username,
                    location="location",
                    linkedin="linkedin",
                    disc="disc",
                    profile_pic="profile_pic",
                    )
            arguments = {}
            arguments['mnm'] = "Try to login with your new account"
            return redirect('/')
        except IntegrityError as e:
            arguments = {}
            arguments['mnm'] = "Username exist"
            return TemplateResponse(request, 'auth/RegisterForm.html', arguments)
    else:
            arguments = {}
            arguments['mnm'] = ""
            return TemplateResponse(request, 'auth/RegisterForm.html', arguments)


def logout(request):
    if request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

        #messages.info(request, "Logged out succesfully!")
