from django.urls import path

from .views import createproject,searchproject

urlpatterns = [
    path('createproject', createproject),
    path('searchproject',searchproject)
]