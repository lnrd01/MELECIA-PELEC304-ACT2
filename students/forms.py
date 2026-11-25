from django import forms
from .models import Student

INPUT = ("w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm "
         "focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200")

SECTIONS = [
    ("Personal Information", ["student_number", "first_name", "middle_name", "last_name",
                              "birth_date", "gender", "nationality", "religion"]),
    ("Contact Information", ["email", "phone", "address"]),
    ("Background Information", ["guardian_name", "guardian_relationship", "guardian_contact",
                                "previous_school", "year_graduated", "honors"]),
    ("Enrollment Information", ["program", "year_level", "section", "status"]),
]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["date_enrolled"]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "address": forms.Textarea(attrs={"rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs["class"] = INPUT

    def sections(self):
        return [(title, [self[n] for n in names]) for title, names in SECTIONS]
