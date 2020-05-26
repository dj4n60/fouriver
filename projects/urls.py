from django.urls import path

from .views import createproject
from .views import profilepage

urlpatterns = [
    path('createproject', createproject),
    path('profilepage', profilepage)

]