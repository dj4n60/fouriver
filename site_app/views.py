from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users

def index(request):
    user_list = Users.objects.all()
    bool_ansers = Users.objects.filter(username="Elias",password = 1234).exists()
    if bool_ansers:
        template = loader.get_template('site_app/blog.html')
        context = {
            'user_list': user_list,
            }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(str(bool_ansers) + " Den paizei tetoio onoma")
    #return render(request, "site_app/blog.html")

