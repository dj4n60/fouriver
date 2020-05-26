from django.urls import path

from .views import createproject, searchproject, toprojectpage, profilepage

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage),
    path('createproject', createproject),
    path('searchproject', searchproject),
    path('toprojectpage', toprojectpage)
]