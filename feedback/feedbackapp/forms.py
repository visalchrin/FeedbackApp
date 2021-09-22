from django import forms
from .models import *


# edit profile form
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['profile']


# edit personal inforamtion form
class EditPersonalForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'department', 'year']


# Add new course form
class AddNewCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['course_name', 'description',
                  'course_photo', 'academic', 'Lecturer']


# Add new lecturer form
class AddNewLecturerForm(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = ['Lecturer_name', 'lecturer_profile', 'lecturer_skill']
