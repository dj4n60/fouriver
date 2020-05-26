from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import IntegrityError

from .models import projects
from .models import user
from django.template.response import TemplateResponse

# Create your views here.
def createproject(request):
    if request.method == 'POST':
        if request.POST.get('jobtitle') and request.POST.get('job-type') and request.POST.get('payment-type') and request.POST.get('jobdescription'):
            Projects = projects()
            Projects.jobtitle = request.POST.get('jobtitle')
            Projects.jobtype = request.POST.get('job-type')
            Projects.paymentmethod = request.POST.get('payment-type')
            Projects.jobdescription = request.POST.get('jobdescription')
            Projects.save()

            return render(request, 'CreateProject.html')

    else:
        return render(request, 'CreateProject.html')



#profile view (it has to get the search data to pass dynamically to html file)
def profilepage(request):

    user1 = user()
    user1.username = 'test'
    user1.location = 'test'
    user1.birthday = 'test'
    user1.gmail = 'test'
    user1.twlink = 'test'
    user1.fblink = 'test'
    user1.gitlink = 'test'

    return render(request, "Profile.html", {'user1': user1})



def searchproject(request):
    if request.method == 'POST':
        if request.POST.get('ProjectTitle') :
            jobtitle = request.POST.get('ProjectTitle')
            Projects = projects.objects.filter(jobtitle=jobtitle)
            return render(request, 'ProjectListing.html',{'Projects':Projects})
        else:
            return HttpResponse("<p> No input </p> ")
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}
    else:
        allprojects = projects.objects.all()
        return render(request, 'MainPage.html', {'allprojects': allprojects})

def toprojectpage(request):
    if request.method == 'POST':
        jobtitle = request.POST.get('jobtitle')
        Projects = projects.objects.filter(jobtitle=jobtitle)
        return render(request, 'ProjectPage.html' , {'Projects':Projects})
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}
    else:
        return render(request, 'ProjectListing.html')