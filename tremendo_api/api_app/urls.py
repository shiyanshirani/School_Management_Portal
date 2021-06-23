from django.urls import path
from .api import StudentCreateApi, TeacherCreateApi, BatchCreateApi,\
                StudentApi, TeacherApi, BatchApi,\
                StudentUpdateApi, TeacherUpdateApi, BatchUpdateApi,\
                StudentDeleteApi, TeacherDeleteApi, BatchDeleteApi
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('students/', views.student_operations, name='student-details'),
    path('students/crud/<int:pk>/', views.student_changes, name='Student-changes'),

    path('teachers/', views.teacher_operations, name='teacher-details'),
    path('teachers/crud/<int:pk>/', views.teacher_changes, name="teacher-changes"),

    path('batch/', views.batch, name="batch-details"),

    path('api/token/', TokenObtainPairView.as_view(), name="get-token"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh-token")
]