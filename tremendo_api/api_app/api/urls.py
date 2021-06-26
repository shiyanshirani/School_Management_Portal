from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('students/', views.student, name='student-details'),
    path('students/<int:pk>/', views.student_api, name='student-changes'),

    path('teachers/', views.teacher, name='teacher-details'),
    path('teachers/<int:pk>/', views.teacher_api, name="teacher-changes"),

    path('batch/', views.batch, name="batch-details"),

    path('api/token/', TokenObtainPairView.as_view(), name="get-token"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh-token")
]