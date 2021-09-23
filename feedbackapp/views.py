from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.db import IntegrityError
from django.http import HttpResponse
from django.urls import reverse
import os

from .models import User, Student, Academic, Course, Feedback
from django.db.models import Exists, OuterRef
from django.contrib.auth.decorators import login_required, permission_required

from .forms import *
# Create your views here.


def index(request):
    return render(request, "feedbackapp/index.html")


# student dashboard view
@login_required(login_url='index')
def student_dashboard(request, username):
    if request.method == "GET":
        if request.user.is_student:
            student = Student.objects.get(user=request.user)
            academic = student.academic
            courses = Course.objects.annotate(is_feedback=Exists(Feedback.objects.filter(
                user=request.user, course_id=OuterRef('pk')))).filter(academic=academic).order_by('-id')

            return render(request, "feedbackapp/dashboard.html", {
                "courses": courses
            })
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# login view
def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_student:
                return HttpResponseRedirect(reverse("student_dashboard", args=(request.user.username,)))
            elif user.is_schoolAdmin:
                return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Invalid Username or/and password",
                "message": "Try again! Make sure you input username and password correctly."
            })
    else:
        return render(request, "feedbackapp/message.html", {
            "message_title": "This request method is not allowed",
            "message": "Make sure you used only platform in the right way."
        })


# course feedback view
@login_required(login_url='index')
def course_feedback(request, course_name):
    if request.method == "GET":
        if request.user.is_schoolAdmin:
            course = Course.objects.get(course_name=course_name)
            feedbacks = Feedback.objects.filter(course=course)

            # the average star of each course
            if not feedbacks:
                rate = 0
            else:
                total = 0
                for feedback in feedbacks:
                    total += feedback.rating
                rate = total / len(feedbacks)

            return render(request, "feedbackapp/feedback.html", {
                "feedbacks": feedbacks,
                "course": course,
                "rate": rate
            })
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# Create course views
@login_required(login_url='index')
def school_admin(request):
    if request.method == "GET":
        if request.user.is_schoolAdmin:
            courseForm = AddNewCourseForm(instance=request.user)
            lecturerForm = AddNewLecturerForm(instance=request.user)
            return render(request, "feedbackapp/course.html", {
                "courseForm": courseForm,
                "lecturerForm": lecturerForm
            })
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# create lecturer view
@login_required(login_url='index')
def create_lecturer(request):
    if request.method == "POST":
        if request.user.is_schoolAdmin:
            newlecturerForm = AddNewLecturerForm(
                request.POST, instance=request.user)
            if newlecturerForm.is_valid():
                data = newlecturerForm.cleaned_data
                lecturer_name = data['Lecturer_name']
                lecturer_profile = request.FILES['lecturer_profile']
                lecturer_skill = data['lecturer_skill']

                newlecturer = Lecturer.objects.create(
                    Lecturer_name=lecturer_name, lecturer_profile=lecturer_profile, lecturer_skill=lecturer_skill)
                newlecturer.save()
                return HttpResponseRedirect(reverse("school_admin"))
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# Create course view
@login_required(login_url='index')
def create_course(request):
    if request.method == "POST":
        if request.user.is_schoolAdmin:
            newCourseForm = AddNewCourseForm(
                request.POST, instance=request.user)
            if newCourseForm.is_valid():
                data = newCourseForm.cleaned_data
                course_name = data['course_name']
                course_photo = request.FILES['course_photo']
                description = data['description']
                academic = data['academic']
                lecturer = data['Lecturer']

                newCourse = Course.objects.create(
                    course_name=course_name, course_photo=course_photo, academic=academic, Lecturer=lecturer)
                newCourse.save()
                return HttpResponseRedirect(reverse("school_admin"))
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# admin dashboard view
@login_required(login_url='index')
def admin_dashboard(request):
    if request.method == "GET":
        if request.user.is_schoolAdmin:
            courses = Course.objects.all()
            return render(request, "feedbackapp/admin_dashboard.html", {
                "courses": courses
            })
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "You are not allowed to access this page."
            })


# logout view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Register view
def register(request):
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        email = request.POST["email"]
        department = request.POST["department"]
        year = request.POST["years"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm = request.POST["confirm-password"]

        if not first_name or not last_name or not email or not department or not year or not username or not password or not confirm:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Invalid input.",
                "message": "Make sure you input all the requirement fields."
            })

        if password != confirm:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Password does not match",
                "message": "Please, check your password and confirm password carefully."
            })
        else:
            try:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, username=username, password=password, is_student=True)
                user.save()

                user = User.objects.get(username=username)
                academic = Academic.objects.get(year=year,
                                                department=department)
                student = Student.objects.create(
                    user=user, first_name=first_name, last_name=last_name, email=email, department=department, year=year, academic=academic)
                student.save()
                return render(request, "feedbackapp/message.html", {
                    "message": "Register success."
                })
            except IntegrityError as e:
                print(e)
                return render(request, "feedbackapp/message.html", {
                    "message_title": "Username already exist!",
                    "message": "Try create an account with other username."
                })
    else:
        return render(request, "feedbackapp/message.html", {
            "message_title": "Request method is not allowed",
            "message": "Make sure you using our platform in the right way."
        })


# about page view
def about(request):
    if request.method == "GET":
        return render(request, "feedbackapp/about.html")


# profile page view
@login_required(login_url='index')
def profile(request, username):

    if request.method == 'GET':
        if request.user.is_student:

            # get login user
            user = User.objects.get(id=request.user.id)
            student = Student.objects.get(user=user)
            editProfileForm = EditProfileForm()
            editPersonalForm = EditPersonalForm(
                initial={'first_name': student.first_name, 'last_name': student.last_name, 'email': student.email, 'department': student.department, 'year': student.year})

            student = Student.objects.get(user=user)
            return render(request, 'feedbackapp/profile.html', {
                "editProfileForm": editProfileForm,
                "editPersonalForm": editPersonalForm,
                "users": user,
                "student": student
            })
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# edit personal information view
@login_required(login_url='index')
def edit_personal(request, username):
    if request.method == "POST":
        if request.user.is_student:
            editPersonalForm = EditPersonalForm(
                request.POST, instance=request.user)
            if editPersonalForm.is_valid():
                data = editPersonalForm.cleaned_data
                first_name = data['first_name']
                last_name = data['last_name']
                email = data['email']
                department = data['department']
                year = data['year']
                student = Student.objects.get(user=request.user)
                student.first_name = first_name
                student.last_name = last_name
                student.email = email
                student.department = department
                student.year = year
                student.save()
            return HttpResponseRedirect(reverse('profile', args=(username,)))
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# edit profile view
@login_required(login_url='index')
def edit_profile(request, username):

    if request.method == 'POST':
        if request.user.is_student:

            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                if request.FILES.get('profile', None) != None:
                    user = User.objects.get(username=username)
                    student = Student.objects.get(user=user)
                    student.profile.delete(False)
                    student.profile = request.FILES['profile']
                    student.save()
                return HttpResponseRedirect(reverse("profile", args=(username,)))
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })
    else:
        if request.user.is_student:
            form = EditProfileForm(instance=request.user)
            return render(request, 'feedbackapp/profile.html', {'form': form})
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })


# Feedback views
@login_required(login_url='index')
def feedback(request, username, course_name):

    if request.method == "POST":
        if request.user.is_student:
            rating = request.POST["rating"]
            message = request.POST["message"]
            user = request.user
            lecturerId = request.POST["lecturerId"]
            courseId = request.POST["courseId"]

            lecturer = Lecturer.objects.get(pk=lecturerId)
            course = Course.objects.get(pk=courseId)
            feedback = Feedback.objects.create(
                rating=rating, message=message, Lecturer=lecturer, course=course, user=user)
            feedback.save()
            return HttpResponseRedirect(reverse("student_dashboard", args=(username,)))
        else:
            return render(request, "feedbackapp/message.html", {
                "message_title": "Private Page",
                "message": "Sorry, you are not allowed to access this page."
            })
