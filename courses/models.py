from django.db import models
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('student', 'course')
        
# class User(models.Model):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=64)
#     pwd = models.CharField(max_length=64)
#     _time = models.DateTimeField(auto_now_add=True)

# def _str_(self):
#     return self.email

# class Meta:
#     ordering = ['-_time']
#     verbose_name = '用戶資料庫'
#     verbose_name_plural = '用戶資料庫'