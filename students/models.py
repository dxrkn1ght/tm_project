from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('Select Gender', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"