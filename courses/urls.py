from django.urls import path,include
from . import views  
from .views import enroll_page
from .views import course_list_page
from .views import add_course_page
from .views import api_root

urlpatterns = [
    path("enroll", enroll_page),
    path("course_list", course_list_page),
    path("add_course", add_course_page),
    path('api/', views.api_root,name='api-root'),  
    path('api/teachers/', views.TeacherListCreateView.as_view(),name='teacher-list'),
    path('api/students/', views.StudentListCreateView.as_view(),name='student-list'),
    path('api/courses/', views.CourseListCreateView.as_view(),name='course_list'),
    path('api/courses/<int:pk>/', views.CourseRetrieveUpdateDestroyView.as_view(),name='course-detail'),
    path('api/enrollments/', views.EnrollmentListView.as_view(),name='enrollment-list'),
    path('api/enroll/', views.EnrollmentCreateView.as_view(),name='enrollment-create'),
]
