from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Teacher, Student, Course, Enrollment
from .serializers import TeacherSerializer, StudentSerializer, CourseSerializer, EnrollmentSerializer
from django.http import HttpResponse
from django.shortcuts import render

@api_view(['GET'])
def api_root(request):
    return Response({
        "teachers": "/api/teachers/",
        "students": "/api/students/",
        "courses": "/api/courses/",
        "enrollments": "/api/enrollments/",
        "enroll": "/api/enroll/"
    })
def course_list_page(request):
    return render(request, "course_list.html")

def add_course_page(request):
    return render(request, "add_course.html")

def user_manage(request):
    return HttpResponse("This is the User Management page.")

def course_manage(request):
    return HttpResponse("這是課程管理頁面")

def course_enroll(request):
    return HttpResponse("這是課程註冊頁面")

def course_create(request):
    return HttpResponse("這是建立課程的頁面")

def enroll_page(request):
    return render(request, "enroll.html")

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.select_related('teacher').all()
    serializer_class = CourseSerializer

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.select_related('teacher').all()
    serializer_class = CourseSerializer

class EnrollmentCreateView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')

        if not student_id or not course_id:
            return Response({"error": "缺少學生或課程 ID"}, status=status.HTTP_400_BAD_REQUEST)

        if not Student.objects.filter(id=student_id).exists():
            return Response({"error": "找不到學生 ID"}, status=status.HTTP_400_BAD_REQUEST)
        if not Course.objects.filter(id=course_id).exists():
            return Response({"error": "找不到課程 ID"}, status=status.HTTP_400_BAD_REQUEST)

        if Enrollment.objects.filter(student_id=student_id, course_id=course_id).exists():
            return Response({"error": "學生已報名此課程"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.select_related('student', 'course').all()
    serializer_class = EnrollmentSerializer

# from django.shortcuts import render ,redirect
# from . import models
# Create your views here.
# def index(request):
#     return render(request,'./login/index.html')

# def login(request):
#      return render(request,'./login/login.html')

# def register(request):
#      if request.method == "POST":
#           email = request.POST.get('email', None)
#           name = request.POST.get('name', None)
#           pwd = request.POST.get('pwd', None)
#           if pwd == pwd:
#             user = models.Users.objects.filter(email=email)
#             if user:
#                 print('帳戶已經被註冊，請重新註冊')
#                 return redirect('/register/')
#             new_user = models.Users.objects.create()
#             new_user.email = email
#             new_user.name = name
#             new_user.pwd = pwd
#             new_user.save()
#             return redirect('/login/')
#      return render(request,'./login/register.html')

# def logout(request):
#     return redirect('/')