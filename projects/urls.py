from django.urls import path


from .views import createproject, searchproject,  profilepage, projectdetails, edit_profile_info

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage),
    path('createproject', createproject),
    path('', searchproject),
    path('createproject', createproject, name="createproject"),
    path('searchproject', searchproject),
    path('projectdetails/<str:pk>/', projectdetails, name="projectdetails"),
    path('editinfo', edit_profile_info),


]
