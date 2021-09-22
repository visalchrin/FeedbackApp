from typing import AbstractSet
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Lecturer(models.Model):
    Lecturer_name = models.CharField(max_length=100)
    lecturer_profile = models.ImageField(
        upload_to='lecturers/', default='default.jpg')
    lecturer_skill = models.CharField(max_length=200, default="Master degree")

    def __str__(self):
        return f"Lecturer: {self.Lecturer_name}"


class Academic(models.Model):
    academic_year = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return f"Academic: {self.academic_year} Year: {self.year}"


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=200, default="Fundamental Course")
    course_photo = models.ImageField(
        upload_to='courses/', default='default.jpg')
    academic = models.ForeignKey(Academic, on_delete=models.CASCADE)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Course: {self.course_name}"


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_schoolAdmin = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    year = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    profile = models.ImageField(
        upload_to='images/', default='default.jpg')
    academic = models.ForeignKey(Academic, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} : {self.department}"


class Feedback(models.Model):
    rating = models.IntegerField()
    message = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} feedback: {self.message} on {self.Lecturer.Lecturer_name}"
