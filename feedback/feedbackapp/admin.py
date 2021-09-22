from django.contrib import admin

from .models import User, Lecturer, Course, Feedback, Academic, Student
# Register your models here.

admin.site.register(User)
admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(Feedback)
admin.site.register(Academic)
admin.site.register(Student)
