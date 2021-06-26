from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('students/', views.StudentList.as_view(), name='student-details'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student-details'),

    path('teachers/', views.TeacherList.as_view(), name='teacher-details'),
    path('teachers/<int:pk>', views.TeacherDetail.as_view(), name="teacher-changes"),

    path('batch/', views.BatchList.as_view(), name="batch-details"),

    path('api/token/', TokenObtainPairView.as_view(), name="get-token"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="refresh-token")
]