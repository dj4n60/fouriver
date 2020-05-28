from django.urls import path

from .views import createproject,searchproject,projectdetails

urlpatterns = [
    path('createproject', createproject, name="createproject"),
    path('searchproject',searchproject),
    path('projectdetails/<str:pk>/',projectdetails,name="projectdetails"),
]