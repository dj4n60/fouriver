from django.core.files.uploadhandler import FileUploadHandler

from .Calls import Calls
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.db.models import Q
from django.db import IntegrityError
from auth.models import appusers
from .models import *
from .models import user
from django.template.response import TemplateResponse
from django import forms
from .forms import EditDeveloperForm, EditCustomerForm


# Create your views here.
def createproject(request):
    if request.method == 'POST':
        if request.POST.get('jobtitle') and request.POST.get('privacytype') and  request.POST.get('job-type') and request.POST.get('payment-type') and request.POST.get('category-type')  and  request.POST.get('jobdescription') :
            Projects = projects()
            Projects.jobtitle = request.POST.get('jobtitle')
            Projects.jobtype = request.POST.get('job-type')
            Projects.paymentmethod = request.POST.get('payment-type')
            Projects.jobdescription = request.POST.get('jobdescription')
            Projects.category= request.POST.get('category-type')
            Projects.privacy = request.POST.get('privacytype')
            Projects.createdby =request.session.get("username")
            Projects.save()

            return redirect('/')
        else:
            return HttpResponse("You have left empty fields")
    else:
        return render(request, 'CreateProject.html')


# profile view (it has to get the search data to pass dynamically to html file)
def profilepage(request):  # (request,username):
    callobject = Calls()
    user1 = callobject.profilecall(request)
    #showing project created by client
    #myProjects = projects.objects.filter(createdby=request.session.get("username"))
    context = {'user1':user1 }
    return render(request, "ProfilePage.html", context)


def searchproject(request):
    arguments = {}
    arguments['mnm'] = ''
    if request.method == 'POST':
        if "SearchP" in request.POST:
            if request.POST.get('projecttext'):
                textinjob = request.POST.get('projecttext')
                mainCategory = request.POST.get('projectcategory')
                criterion1 = Q(jobtitle__exact=textinjob)
                criterion2 = Q(jobtype__icontains=mainCategory)
                if request.session.get('username'):
                    allProjects = projects.objects.filter(criterion1 | criterion2 )
                    return render(request, 'ProjectListing.html', {'Projects': allProjects})  # contains the text
                else:
                    publicProjects = projects.objects.filter(Q(privacy="Public") & criterion1)
                    return render(request, 'ProjectListing.html', {'Projects': publicProjects})  # contains the text
            else:
                arguments['mnm'] = "! Place at least one keyword !"
                return render(request, 'MainPage.html', arguments)

        elif "SearchU" in request.POST:
            if request.POST.get('username'):
                user = request.POST.get('username')
                cat = request.POST.get('usertype')
                return render(request, 'ProjectListing.html', {'Projects': Projects})
            else:
                return render(request, 'MainPage.html', {'mnm': mnm})
        elif "profile" in request.POST:
            if request.session.get('username'):
                callobject = Calls()
                user1 = callobject.profilecall(request)
                return render(request, "ProfilePage.html", {'user1': user1})
            else:
                arguments['mnm'] = "! You have to log in to see your profile click the register buttom !"
                return render(request, 'MainPage.html', arguments)
        else:
            return HttpResponse("<p> No input </p> ")
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}
    else:
        if request.session.get('username'):
            allprojects = projects.objects.all()[:4]
            return render(request, 'MainPage.html', {'allprojects': allprojects})
        else:
            # showing only public projects
            publicprojects = projects.objects.filter(privacy="Public")[:4]
            return render(request, 'MainPage.html', {'allprojects': publicprojects})



#projectlisting
#def toprojectpage(request):
        #jobtitle = request.POST.get('jobtitle')
        #Projects = projects.objects.filter(jobtitle=jobtitle)
        #return render(request, 'ProjectPage.html' , {'Projects':Projects})
    #Projects in {} refer to html / data passed to html
    #Projects = projects.objects.filter(jobtitle=jobtitle)
    #context = {'Projects':Projects}


def edit_profile_info(request):
    if request.session.get('idiotita') == 'developer':
        form = EditDeveloperForm(request.POST, request.FILES )
        context = {
            'form': form
        }
        if request.method == "POST":
            if form.is_valid():

                username = request.session.get('username')
                location = request.POST.get('location')
                language = request.POST.get('language')
                github = request.POST.get('github')
                cv = request.POST.get('cv')
                profile_pic = request.POST.get('profile_pic')
                new = form.save()
                new.profile_pic = request.FILES.get('profile_pic')
                try:
                    userinfo = developerinfo.objects.create(
                        username=request.session.get('username'),
                        location=location,
                        language=language,
                        github=github,
                        cv=cv,
                        profile_pic=profile_pic,
                    )
                    arguments = {}
                    arguments['mnm'] = "all done"
                    return redirect(profilepage, arguments)
                except IntegrityError as e:
                    arguments = {}
                    arguments['mnm'] = "sth went wrong"
                    return TemplateResponse(request, 'EditDeveloperInfo.html', arguments)

        return render(request, 'EditDeveloperInfo.html', context)
    if request.session.get('idiotita') == 'client':
        form = EditCustomerForm(request.POST, request.FILES or None)
        context = {
            'form': form
        }
        if request.method == 'POST':
            if form.is_valid():

                username = request.session.get('username')
                location = request.POST.get('location')
                linkedin = request.POST.get('linkedin')
                disc = request.POST.get('disc')
                profile_pic = request.POST.get('profile_pic')
                new = form.save()
                new.profile_pic = request.FILES.get('profile_pic')

                try:
                    userinfo = customerinfo.objects.create(
                        username=request.session.get('username'),
                        location=location,
                        linkedin=linkedin,
                        disc=disc,
                        profile_pic=profile_pic,
                    )
                    arguments = {}
                    arguments['mnm'] = "all done"
                    return redirect(profilepage, arguments)
                except IntegrityError as e:
                    arguments = {}
                    arguments['mnm'] = "sth went wrong"
                    return TemplateResponse(request, 'EditCustomerInfo.html', arguments)


        return render(request, 'EditCustomerInfo.html', context)


def projectdetails(request,pk):
    Offers = offers.objects.filter(projectid=pk)
    totalOffers =Offers.count()
    Projects = projects.objects.get(id=pk)
    Comments = comments.objects.filter(projectid=pk)
    if request.session.get('username'):
        if Projects.createdby == request.session.get('username'):
            context = {'Projects': Projects ,'Offers' : Offers ,'totalOffers':totalOffers,'Comments':Comments}
            return render(request, 'ProjectPage.html', context)
        else:
            context = {'Projects': Projects, 'totalOffers': totalOffers,'Comments':Comments}
            return render(request, 'ProjectPage.html', context)
    #pk is called in the url path
    else:
        return render(request, 'ProjectPage.html',{'Projects':Projects,'Comments':Comments})


def myprojects(request):
    if request.session.get('username'):
        #check if client or developer
        if request.session['idiotita'] == 'client':

            myProjects = projects.objects.filter(createdby=request.session.get("username"))
            return render(request, 'MyProjects.html', {'myProjects': myProjects})
        else:
            myProjects = projects.objects.filter(offerby=request.session.get("username"))
            return render(request, 'MyProjects.html', {'myProjects': myProjects})
    else:
        return HttpResponse("You are not logged in")

def apply(request,pk):
    if request.method == 'POST':
        if request.POST.get('project_id') and request.POST.get('money') and request.POST.get('project_title'):
            Offers = offers()
            Offers.projectid = request.POST.get('project_id')
            Offers.developername = request.session.get("username")
            Offers.projecttitle = request.POST.get('project_title')
            Offers.money = request.POST.get('money')

            Offers.save()

            return redirect('/')
        else:
            return HttpResponse("Data not saved")

    #check if client or developer
    else:
        if request.session['idiotita'] == 'developer':
                #if offers.objects.get(Q(projectid=pk) & Q(developername=request.session.get('username'))):
                    #HttpResponse("You have already submited an offer for this project")
            Offers = offers.objects.filter(Q(projectid=pk) & Q(developername=request.session.get('username'))).count()
            if Offers > 0 :
                html = "You have already made an offer for this projects go to  " + '<a href="/myoffers">My Offers</a>' + "  to delete previous offer in order to make a new one"
                return HttpResponse(html)
            else:
                Projects = projects.objects.get(id=pk)
                context = {'Projects': Projects}
                return render(request, 'ApplyPage.html', context)
        else:
            return HttpResponse("You are not a developer")




def reccomend(request,pk):
    if request.method == 'POST':
        if request.POST.get('project_id') and request.POST.get('project_title') and request.POST.get('developername'):
            Reccomends=reccomends()
            Reccomends.projectid = request.POST.get('project_id')
            Reccomends.projecttitle = request.POST.get('project_title')
            Reccomends.developername = request.POST.get('developername')
            Reccomends.reccomendedby = request.session.get("username")

            Reccomends.save()
            return redirect('/')

        else:
            return HttpResponse("You left empty fields")

    else:       #filtering users
        Projects = projects.objects.get(id=pk)
        Users = appusers.objects.filter(idiotita="developer")
        context = {'Projects': Projects , 'Users': Users}
        return render(request, 'ReccomendPage.html', context)



def acceptoffer(request,pk,sk):
    #pk,sk in url path
    if request.method == 'POST':
        if request.POST.get('project_id') and request.POST.get('developer_name'):
            Offers = offers.objects.get(id=sk)
            Projects = projects.objects.get(id=pk)
            Projects.offerby = request.POST.get('developer_name')
            Projects.isCompleted = True
            Offers.isAccepted = True
            Projects.save()
            Offers.save()
            return redirect('/')
        else:
            return HttpResponse("Attributes empty")
    else:
        Projects = projects.objects.get(id=pk)
        Offers = offers.objects.get(id=sk)
        context = {'Projects': Projects , 'Offers':Offers}
        return render(request ,'AcceptOfferPage.html',context)

def myreccomendations(request):
    total_reccomendations = reccomends.objects.filter(developername=request.session.get("username")).count()
    if total_reccomendations>0 :
        myReccomedations = reccomends.objects.filter(developername=request.session.get("username"))
        return render(request, 'MyReccomendations.html', {'myReccomendations': myReccomedations})
    else:
        return HttpResponse("You have no reccomendations yet")



def myoffers(request):
    Offers = offers.objects.filter(Q(developername=request.session.get('username')) & Q(isAccepted=False)).count()
    if Offers>0 :
        myOffers =offers.objects.filter(Q(developername=request.session.get('username')) & Q(isAccepted=False))
        return render(request,'MyOffers.html', {'myOffers': myOffers})
    else:
        return HttpResponse("You have made no pending offers.Either you have deleted offers or client has accepted your offers")


def deleteoffer(request,pk):
    if request.method == 'POST':
        myOffer = offers.objects.get(id=pk)

        myOffer.delete()
        return redirect('/')
    else:
        myOffer = offers.objects.get(Q(id=pk) & Q(isAccepted=False))
        return render(request, 'DeleteOffer.html', {'myOffer': myOffer})

def completeprojectdeveloper(request,pk):
    if request.method == "POST":
        if request.POST.get('developer_comments'):
            Project = projects.objects.get(id=pk)
            Project.developercomments = request.POST.get('developer_comments')
            Project.isCompletedbyDeveloper = True

            Project.save()
            return redirect('/')
        else:
            return HttpResponse("Comment section is empty")
    else:
        Project=projects.objects.get(id=pk)
        return render(request,'CompleteProjectDeveloper.html',{'Project':Project})

def comment(request,pk):
    if request.method == "POST":
        if request.POST.get('comments'):
            Comment = comments()
            Comment.commentby = request.session.get("username")
            Comment.projectid = request.POST.get('project_id')
            Comment.comment = request.POST.get('comments')

            Comment.save()
            return redirect('/')
        else:
            return HttpResponse("Comment section is empty")
    else:
        Project=projects.objects.get(id=pk)
        return render(request,'CommentPage.html',{'Project':Project})

def editproject(request,pk):
    Project = projects.objects.get(id=pk)
    if request.method == "POST":
        Project.jobtitle = request.POST.get('jobtitle')
        Project.privacy = request.POST.get('privacytype')

        Project.save()
        return redirect('/')

    else:
        context = {'Project':Project}
        return render(request,'EditProject.html',context)
