from django.db import models

# Create your models here.

# StudentNews table
class Student(models.Model):
    sno = models.AutoField
    img = models.ImageField(blank=True)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# FacultyNews table
class Faculty(models.Model):
    sno = models.AutoField
    img = models.ImageField(blank=True)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
# EventsNews table
class Event(models.Model):
    sno = models.AutoField
    img = models.ImageField(blank=True)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title
