from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .Auth import Authetic
from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username= request.POST.get('user')
        password= request.POST.get('pass')
        Password = str(password)
        authobject = Authetic(Password)
        return HttpResponse("<p> Welcome </p> " + str(username)+ "<p> password </p>" + str(authobject.encrypt()) )
        #return render(request, 'site_app/blog.html')
    else:
        return render(request, 'auth/LoginForm.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        return HttpResponse("<p> Welcome </p> " + str(username)+ "<p> email </p>" + str(email) )
    else:
        return render(request, 'auth/RegisterForm.html')
