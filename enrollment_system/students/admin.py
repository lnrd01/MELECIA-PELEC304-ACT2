from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "last_name", "first_name", "program", "year_level", "status")
    search_fields = ("student_number", "first_name", "last_name")
    list_filter = ("status", "year_level", "program")
