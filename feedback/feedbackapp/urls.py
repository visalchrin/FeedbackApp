from django.urls import path
from . import views
from django.contrib import admin
# from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("account/login", views.login_view, name="login"),
    path("account/logout", views.logout_view, name="logout"),
    path("account/register", views.register, name="register"),
    path("about", views.about, name="about"),
    path("<str:username>/profile", views.profile, name="profile"),
    path("<str:username>/edit_profile",
         views.edit_profile, name="edit_profile"),
    path("<str:username>/edit_personal",
         views.edit_personal, name="edit_personal"),
    path("<str:username>/dashboard",
         views.student_dashboard, name="student_dashboard"),
    path("<str:username>/<str:course_name>/feedback",
         views.feedback, name="feedback"),
    path("feedback/admin_dashboard", views.admin_dashboard, name="admin_dashboard"),
    path("<str:course_name>/feedbacks",
         views.course_feedback, name="course_feedback"),
    path("school_admin", views.school_admin, name="school_admin"),
    path("crate_course", views.create_course, name="create_course"),
    path("create_lecturer", views.create_lecturer, name="create_lecturer")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
