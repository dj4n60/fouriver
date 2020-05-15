from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import IntegrityError

from .models import projects
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

def searchproject(request):
    if request.method == 'POST':
        jobtitle = request.POST.get('ProjectTitle')
        jobtype = request.POST.get('projectcategory')
        result = projects.objects.filter(jobtitle=jobtitle)
        return render(request, 'ProjectListing.html',{'Projects':result})
    #Projects in {} refer to html
    else:
        return render(request, 'MainPage.html')
