from django.urls import path


from .views import createproject, searchproject,  profilepage, projectdetails, editprofiledev, editprofilecus

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage),
    path('createproject', createproject),
    path('', searchproject),
    path('createproject', createproject, name="createproject"),
    path('searchproject', searchproject),
    path('projectdetails/<str:pk>/', projectdetails, name="projectdetails"),
    path('editprofiledev', editprofiledev), # change path when edit profile htmls are finished
    path('editprofilecus', editprofilecus)
]
