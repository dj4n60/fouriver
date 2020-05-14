from django.urls import path

from .views import createproject

urlpatterns = [
    path('createproject', createproject)
]