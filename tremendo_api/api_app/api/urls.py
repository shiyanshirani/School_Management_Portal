from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('students/', views.StudentList.as_view(), name='student-details'),
    path('students/list/', views.StudentListView.as_view(), name='studentlist_view'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student-details'),

    path('teachers/', views.TeacherList.as_view(), name='teacher-details'),
    path('teachers/list/', views.TeacherListView.as_view(), name='teacherlist_view'),
    path('teachers/<int:pk>', views.TeacherDetail.as_view(), name="teacher-changes"),

    path('batch/', views.BatchList.as_view(), name="batch-list"),
    path('batch/list/', views.BatchListView.as_view(), name="batchlist_view"),
    path('batch/<int:pk>', views.BatchDetail.as_view(), name="batch-details"),

    path('api/token/', TokenObtainPairView.as_view(), name="get-token"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="refresh-token"),

    path('all_profiles/', views.UserProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>', views.userProfileDetailView.as_view(), name="profile"),
]