from django.db import models


class Student(models.Model):
    GENDER = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    YEAR = [(1, "1st Year"), (2, "2nd Year"), (3, "3rd Year"), (4, "4th Year")]
    STATUS = [("Enrolled", "Enrolled"), ("Pending", "Pending"), ("Dropped", "Dropped")]

    # Personal info
    student_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    nationality = models.CharField(max_length=40, default="Filipino")
    religion = models.CharField(max_length=60, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField()

    # Background info
    guardian_name = models.CharField(max_length=120)
    guardian_relationship = models.CharField(max_length=40)
    guardian_contact = models.CharField(max_length=20)
    previous_school = models.CharField(max_length=150, blank=True)
    year_graduated = models.PositiveSmallIntegerField(null=True, blank=True)
    honors = models.CharField(max_length=100, blank=True)

    # Enrollment info
    program = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField(choices=YEAR, default=1)
    section = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default="Pending")
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.student_number} - {self.full_name}"

    @property
    def full_name(self):
        mid = f" {self.middle_name[0]}." if self.middle_name else ""
        return f"{self.first_name}{mid} {self.last_name}"

    @property
    def initials(self):
        return (self.first_name[:1] + self.last_name[:1]).upper()
