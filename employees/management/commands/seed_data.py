from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed database with fake employees, attendance, and performance data'

    def handle(self, *args, **kwargs):
        # Import models inside the handle method to avoid AppRegistryNotReady errors
        from employees.models import Department, Employee
        from attendance.models import Attendance
        from performance.models import Performance

        fake = Faker()
        # Create departments
        departments = ['Engineering', 'HR', 'Sales', 'Finance', 'Marketing']
        dept_objs = []
        for name in departments:
            dept_objs.append(Department.objects.get_or_create(name=name)[0])

        # Create employees
        employees = []
        for _ in range(50):
            dept = random.choice(dept_objs)
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=dept
            )
            employees.append(emp)

        # Create attendance records
        for emp in employees:
            for i in range(60):  # last 60 days
                date = datetime.today().date() - timedelta(days=i)
                status = random.choices(
                    ['present', 'absent', 'late'],
                    weights=[0.8, 0.1, 0.1],
                    k=1
                )[0]
                Attendance.objects.create(employee=emp, date=date, status=status)

        # Create performance records
        for emp in employees:
            for _ in range(3):  # three reviews
                review_date = fake.date_between(start_date=emp.date_of_joining, end_date='today')
                rating = random.randint(1, 5)
                Performance.objects.create(employee=emp, rating=rating, review_date=review_date)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
