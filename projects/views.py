from .Calls import Calls
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import IntegrityError
from auth.models import appusers
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


# profile view (it has to get the search data to pass dynamically to html file)
def profilepage(request):  # (request,username):
    callobject = Calls()
    user1 = callobject.profilecall(request)
    return render(request, "ProfilePage.html", {'user1': user1})



def searchproject(request):
    arguments = {}
    arguments['mnm'] = ''
    if request.method == 'POST':
        if "SearchP" in request.POST:
            if request.POST.get('projecttext') :
                #     Απλό κείμενο. Το σύστημα θα ψάχνει στον τίτλο και στην περιγραφή και θα φέρνει τα αποτελέσματα στο χρήστη.
                #     Σύνθετη αναζήτηση:
                #     Βάσει προτεινόμενων τεχνολογιών.
                #     Βάσει ημερομηνίας υποβολής.
                #     Βάσει κατηγορίας.
                #     Βάσει υποκατηγορίας.

                textinjob = request.POST.get('projecttext')

                Projects = projects.objects.filter(jobtitle=textinjob)
                return render(request, 'ProjectListing.html',{'Projects':Projects})
            else:
                return render(request, 'MainPage.html')

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
        allprojects = projects.objects.all()
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
    context = {'Projects':Projects}
    return render(request, 'ProjectPage.html',context)
