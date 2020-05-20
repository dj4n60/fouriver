from django.urls import path

from .views import createproject,searchproject,toprojectpage

urlpatterns = [
    path('createproject', createproject),
    path('searchproject',searchproject),
    path('toprojectpage',toprojectpage)
]