from django.urls import path
from . import views

urlpatterns = [
    path("", views.gate, name="gate"),
    path("guest/", views.guest_enter, name="guest"),
    path("logout/", views.logout_view, name="logout"),
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.student_add, name="student_add"),
    path("students/<int:pk>/", views.student_list, name="student_detail"),
    path("students/<int:pk>/edit/", views.student_edit, name="student_edit"),
]
