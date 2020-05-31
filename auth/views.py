from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .Auth import Authetic
from django.db import IntegrityError
from .models import appusers
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
            return HttpResponse("<p> Welcome you are gonna see your profile soon </p> ")

        else:
            arguments = {}
            arguments['mnm'] = "! Wrong Password or Username !"
            return TemplateResponse(request, 'auth/LoginForm.html', arguments)
    else:
        return render(request, 'auth/LoginForm.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        idiotita = request.POST.get('member_level')
        Password = str(password)
        authobject = Authetic(Password)
        try:
            newuser = appusers.objects.create(username=username,password=str(authobject.encrypt()),email=email,idiotita=idiotita)
            return HttpResponse("<p> Register </p> " + str(username)+ "<p> Me idiotita </p>" + str(idiotita) + str(newuser))
        except IntegrityError as e:
            arguments = {}
            arguments['mnm'] = "--------------Username Already Exist-----------------"
            return TemplateResponse(request, 'auth/RegisterForm.html', arguments)
    else:
            arguments = {}
            arguments['mnm'] = ""
            return TemplateResponse(request, 'auth/RegisterForm.html', arguments)


def logout_request(request):
    if request.method == 'POST':
        request.session.flush()
        messages.info(request, "Logged out succesfully!")
        return render(request, 'auth/LoginForm.html')