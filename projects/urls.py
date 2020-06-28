from django.urls import path


from .views import createproject, searchproject,  profilepage, projectdetails,myprojects , apply , reccomend ,acceptoffer,myreccomendations,myoffers,deleteoffer,completeprojectdeveloper,comment,editproject,edit_profile_info

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage),
    path('createproject', createproject),
    path('', searchproject),
    path('createproject', createproject, name="createproject"),
    path('searchproject', searchproject),
    path('projectdetails/<str:pk>/', projectdetails, name="projectdetails"),
    path('editinfo', edit_profile_info),
    path('myprojects', myprojects),
    path('apply/<str:pk>/', apply, name="apply"),
    path('reccomend/<str:pk>/', reccomend, name="reccomend"),
    path('acceptoffer/<str:pk>/<str:sk>', acceptoffer, name="acceptoffer"),
    path('myreccomendations', myreccomendations),
    path('myoffers',myoffers),
    path('deleteoffer/<str:pk>/', deleteoffer, name="deleteoffer"),
    path('completeprojectdeveloper/<str:pk>/', completeprojectdeveloper, name="completeprojectdeveloper"),
    path('editinfo', edit_profile_info),
    path('comment/<str:pk>/', comment, name="comment"),
    path('editproject/<str:pk>/', editproject, name="editproject"),
]
