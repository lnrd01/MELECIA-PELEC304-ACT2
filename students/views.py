from functools import wraps

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import StudentForm
from .models import Student


def access_required(view):
    """Allow logged-in admins OR visitors who chose 'continue without login'."""
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated or request.session.get("guest"):
            return view(request, *args, **kwargs)
        return redirect("gate")
    return wrapper


def admin_required(view):
    """Only logged-in staff can add or edit enrollees."""
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view(request, *args, **kwargs)
        messages.error(request, "Please log in as admin to add or edit enrollees.")
        return redirect("gate")
    return wrapper


def gate(request):
    """Landing page with the login pop-up."""
    if request.user.is_authenticated:
        return redirect("student_list")
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid() and form.get_user().is_staff:
            login(request, form.get_user())
            return redirect("student_list")
        if form.is_valid():
            form.add_error(None, "This account is not an admin account.")
    for f in form.fields.values():
        f.widget.attrs["class"] = ("w-full rounded-lg border border-slate-300 px-3 py-2 text-sm "
                                   "focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200")
    return render(request, "students/gate.html", {"form": form})


@require_POST
def guest_enter(request):
    request.session["guest"] = True
    return redirect("student_list")


def logout_view(request):
    logout(request)
    return redirect("gate")


@access_required
def student_list(request, pk=None):
    q = request.GET.get("q", "").strip()
    students = Student.objects.all()
    if q:
        students = students.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(student_number__icontains=q)
        )
    selected = get_object_or_404(Student, pk=pk) if pk else students.first()
    return render(request, "students/list.html", {
        "students": students, "selected": selected, "q": q,
        "total": Student.objects.count(),
    })


@admin_required
def student_add(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        s = form.save()
        messages.success(request, f"{s.full_name} was added.")
        return redirect("student_detail", pk=s.pk)
    return render(request, "students/form.html", {"form": form, "title": "Add Enrollee"})


@admin_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Changes saved.")
        return redirect("student_detail", pk=pk)
    return render(request, "students/form.html", {"form": form, "title": f"Edit {student.full_name}"})
