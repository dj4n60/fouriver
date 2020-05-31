from django.urls import path


from .views import createproject, searchproject, toprojectpage, profilepage,projectdetails

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage),
    path('createproject', createproject),
    path('searchproject', searchproject),
    path('toprojectpage', toprojectpage)
    path('createproject', createproject, name="createproject"),
    path('searchproject',searchproject),
    path('projectdetails/<str:pk>/',projectdetails,name="projectdetails"),

]