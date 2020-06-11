from django.urls import path


from .views import createproject, searchproject,  profilepage, projectdetails, editprofile, editdevs, editcus

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage),
    path('createproject', createproject),
    path('', searchproject),
    path('createproject', createproject, name="createproject"),
    path('searchproject', searchproject),
    path('projectdetails/<str:pk>/', projectdetails, name="projectdetails"),
    path('editprofilepage', editprofile),
    path('editprofiledev', editdevs),# change path when edit profile htmls are finished
    path('editprofilecus', editcus)
]
