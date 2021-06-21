from django.urls import path
from .api import StudentCreateApi


urlpatterns = [
    path('api/create', StudentCreateApi.as_view()),
]