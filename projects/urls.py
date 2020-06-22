from django.urls import path


from .views import createproject, searchproject,  profilepage, projectdetails,myprojects , apply , reccomend ,acceptoffer,myreccomendations

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
    path('reccomend/<str:pk>/', reccomend, name="reccomend"),
    path('acceptoffer/<str:pk>/<str:sk>', acceptoffer, name="acceptoffer"),
    path('myreccomendations', myreccomendations),

]
