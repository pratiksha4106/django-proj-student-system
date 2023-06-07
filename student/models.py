from django.db import models

# Create your models here.
class Student(models.Model):
    Student_ID = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    percentage = models.FloatField()

    def __str__(self):
        return f'Student:{self.first_name}{self.last_name}'


