from django.urls import path


from .views import createproject, searchproject,  profilepage, projectdetails,myprojects , apply

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage),
    path('createproject', createproject),
    path('', searchproject),
    path('createproject', createproject, name="createproject"),
    path('searchproject', searchproject),
    path('projectdetails/<str:pk>/', projectdetails, name="projectdetails"),
    path('myprojects', myprojects),
    path('apply/<str:pk>/', apply, name="apply"),

]
