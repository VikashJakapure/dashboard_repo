from django.db import models

class Student(models.Model):


    name = models.CharField(max_length=30)
    course_id = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name