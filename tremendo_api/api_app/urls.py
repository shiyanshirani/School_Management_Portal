from django.urls import path
from .api import StudentCreateApi, TeacherCreateApi, BatchCreateApi, StudentApi, TeacherApi, BatchApi


urlpatterns = [
    path('student/create', StudentCreateApi.as_view()),
    path('teacher/create', TeacherCreateApi.as_view()),
    path('batch/create', BatchCreateApi.as_view()),

    path('student/', StudentApi.as_view()),
    path('teacher/', TeacherApi.as_view()),
    path('batch/', BatchApi.as_view()),
]