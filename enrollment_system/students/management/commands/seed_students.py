from datetime import date
from django.core.management.base import BaseCommand
from students.models import Student

SAMPLES = [
    ("2026-0001", "Maria", "Santos", "Cruz", date(2006, 3, 14), "Female", "Nagcarlan, Laguna", "BS Information Technology", 1, "A", "Enrolled", "Ana Cruz", "Mother"),
    ("2026-0002", "Juan", "Reyes", "Dela Cruz", date(2005, 11, 2), "Male", "Liliw, Laguna", "BS Computer Science", 2, "B", "Enrolled", "Pedro Dela Cruz", "Father"),
    ("2026-0003", "Angela", "Mendoza", "Bautista", date(2006, 7, 21), "Female", "Rizal, Laguna", "BS Education", 1, "A", "Pending", "Lita Bautista", "Mother"),
    ("2026-0004", "Mark", "Lopez", "Garcia", date(2004, 1, 30), "Male", "Calamba, Laguna", "BS Business Administration", 3, "C", "Dropped", "Rosa Garcia", "Aunt"),
]

class Command(BaseCommand):
    help = "Load a few sample students"

    def handle(self, *args, **opts):
        for n, fn, mn, ln, bd, g, addr, prog, yr, sec, st, gn, gr in SAMPLES:
            Student.objects.get_or_create(student_number=n, defaults=dict(
                first_name=fn, middle_name=mn, last_name=ln, birth_date=bd, gender=g,
                email=f"{fn.lower()}.{ln.lower().replace(' ', '')}@example.com", phone="09171234567",
                address=addr, guardian_name=gn, guardian_relationship=gr, guardian_contact="09181234567",
                previous_school="Nagcarlan National High School", year_graduated=2024, honors="With Honors",
                program=prog, year_level=yr, section=sec, status=st))
        self.stdout.write(self.style.SUCCESS("Sample students loaded."))
