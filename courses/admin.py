from django.contrib import admin
from .models import Teacher, Student, Course, Enrollment
from .import models

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)

