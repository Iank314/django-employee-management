from django.db import models

class Department(models.Model):
    """
    Represents a department within the company.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Represents an employee record.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    date_of_joining = models.DateField()
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees'
    )
    class Meta:
        ordering = ["id"] 
    def __str__(self):
        return f"{self.name} ({self.email})"
