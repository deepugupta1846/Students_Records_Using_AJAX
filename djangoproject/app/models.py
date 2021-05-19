from django.db import models

# Create your models here.
gender=(
    ('Male','Male'),
    ('Female','Female')
)


class Srecord(models.Model):
    Sname = models.CharField(max_length=200)
    Fname = models.CharField(max_length=200)
    Gender = models.CharField(max_length=10, choices=gender)
    Clas = models.CharField(max_length=10)
    Rollno = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.Sname}"
