from django.db import models

# Create your models here.
class Student(models.Model):
    index = models.CharField(max_length=10, unique=True, null=False)
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True, null=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.index + " " + self.firstname + " " + self.lastname + " " + self.email
    
    #def __init__(self, index, firstname, lastname, email):
    #    self.index = index
    #    self.firstname = firstname
    #    self.lastname = lastname
    #    self.email = email

class Professor(models.Model):
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True, null=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname + " " + self.email

    #def __init__(self, firstname, lastname, email):
    #    self.firstname = firstname
    #    self.lastname = lastname
    #    self.email = email