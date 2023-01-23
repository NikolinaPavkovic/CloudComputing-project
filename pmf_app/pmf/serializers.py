from rest_framework import serializers
from .models import Student, Professor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['index', 'firstname', 'lastname', 'email']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['firstname', 'lastname', 'email']