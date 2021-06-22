from django.urls import path
from .api import StudentCreateApi, TeacherCreateApi, BatchCreateApi,\
                StudentApi, TeacherApi, BatchApi,\
                StudentUpdateApi, TeacherUpdateApi, BatchUpdateApi,\
                StudentDeleteApi, TeacherDeleteApi, BatchDeleteApi
from . import views

urlpatterns = [
    # path('student/create', StudentCreateApi.as_view()),
    # path('teacher/create', TeacherCreateApi.as_view()),
    # path('batch/create', BatchCreateApi.as_view()),

    # path('student/', StudentApi.as_view()),
    # path('teacher/', TeacherApi.as_view()),
    # path('batch/', BatchApi.as_view()),

    # path('student/<int:pk>', StudentApi.as_view()), 
    # path('teacher/<int:pk>', TeacherApi.as_view()),
    # path('batch/<int:pk>', BatchApi.as_view()),

    # path('student/<int:pk>/delete', StudentDeleteApi.as_view()), 
    # path('teacher/<int:pk>/delete', TeacherDeleteApi.as_view()), 
    # path('batch/<int:pk>/delete', BatchDeleteApi.as_view()), 

    path('students/', views.student_operations, name='Student-details'),
    path('students/crud/<int:pk>', views.student_delete, name='Student-delete')
]