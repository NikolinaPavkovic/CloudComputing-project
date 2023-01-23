from django.db import models

# Create your models here.
class Student(models.Model):
    index = models.CharField(max_length=10, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.index + " " + self.firstname + " " + self.lastname + " " + self.email


class Professor(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname + " " + self.email
