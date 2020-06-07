from .Calls import Calls
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.db import IntegrityError
from auth.models import appusers
from .models import projects, devinfo, customerinfo
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


# profile view (it has to get the search data to pass dynamically to html file)
def profilepage(request):  # (request,username):
    callobject = Calls()
    user1 = callobject.profilecall(request)
    return render(request, "ProfilePage.html", {'user1': user1})

def editprofiledev(request):
    return render(request, "EditProfileDev.html")


def editprofilecus(request):
    return render(request, "EditProfileCustomer.html")


#
#def editprofile(request):
#   if request.get.session('idiotita') == 'developer':
#       return render(request, "EditProfileDev.html")
#   if request.get.session('idiotita') == 'customer':
#       return render(request, "EditProfileCustomer.html")


def searchproject(request):
    arguments = {}
    arguments['mnm'] = ''
    if request.method == 'POST':
        if "SearchP" in request.POST:
            if  request.POST.get('projecttext'):
                textinjob = request.POST.get('projecttext')
                mainCategory = request.POST.get('projectcategory')
                Projects = projects.objects.filter( Q(jobtitle__exact=textinjob) | Q(jobdescription__exact=textinjob) | Q(jobtype__icontains=mainCategory)  )
                return render(request, 'ProjectListing.html',{'Projects':Projects}) # contains the text
            else:
                arguments['mnm'] = "! Place at least one keyword !"
                return render(request, 'MainPage.html', arguments)

        elif "SearchU" in request.POST:
            if request.POST.get('username'):
                user = request.POST.get('username')
                cat = request.POST.get('usertype')
                return render(request, 'ProjectListing.html',{'Projects':Projects})
            else:
                return render(request, 'MainPage.html', {'mnm': mnm})
        elif "profile" in request.POST:
            if request.session.get('username'):
                callobject = Calls()
                user1 = callobject.profilecall(request)
                return render(request, "ProfilePage.html", {'user1': user1} )
            else:
                arguments['mnm'] = "! You have to log in to see your profile click the register buttom !"
                return render(request, 'MainPage.html', arguments)
        else:
            return HttpResponse("<p> No input </p> ")
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}
    else:
        allprojects = projects.objects.all()[:4]
        return render(request, 'MainPage.html', {'allprojects': allprojects})


#projectlisting
#def toprojectpage(request):
        #jobtitle = request.POST.get('jobtitle')
        #Projects = projects.objects.filter(jobtitle=jobtitle)
        #return render(request, 'ProjectPage.html' , {'Projects':Projects})
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}


def projectdetails(request,pk):
    #pk is called in the url path
    Projects= projects.objects.get(id=pk)
    context = {'Projects': Projects}
    return render(request, 'ProjectPage.html',context)


def editdevs(request):
    if request.method == 'POST':
        location = request.POST.get('city')
        language = request.POST.get('language')
        cv = request.POST.get('cv')
        github = request.POST.get('github')
        profile_pic = request.POST.get('profile_pic')
        try:
            userinfo =devinfo.objects.filter(username=request.session.get('username'), location=location, language=language, cv=cv, github=github, profile_pic=profile_pic)
            arguments = {}
            arguments['mnm'] = "all done"
            return redirect('projects/ProfilePage.html', arguments)
        except IntegrityError as e:
            arguments = {}
            arguments['mnm'] = "sth went wrong"
            return TemplateResponse(request, 'projects/EditProfileDev.html', arguments)
    else:
        arguments = {}
        arguments['mnm'] = ""
        return TemplateResponse(request, 'projects/EditProfileDev.html', arguments)


def editcus(request):
    if request.method == 'POST':
        location = request.POST.get('city')
        disc = request.POST.get('disc')
        linkedin = request.POST.get('linkedin')
        profile_pic = request.POST.get('profile_pic')
        try:
            userinfo = customerinfo.objects.filter(username=request.session.get('username'), location=location, disc=disc, linkedin=linkedin, profile_pic=profile_pic )
            arguments = {}
            arguments['mnm'] = "all done"
            return redirect('projects/ProfilePage.html', arguments)
        except IntegrityError as e:
            arguments = {}
            arguments['mnm'] = "sth went wrong"
            return TemplateResponse(request, 'projects/EditProfileCustomer.html', arguments)
    else:
        arguments = {}
        arguments['mnm'] = ""
        return TemplateResponse(request, 'projects/EditProfileCustomer.html', arguments)
