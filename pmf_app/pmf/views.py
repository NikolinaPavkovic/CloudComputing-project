from django.shortcuts import render
from .models import Student, Professor

# Create your views here.
def index(request):
    return render(request, 'pmf/index.html')

def add_student(request):
    return render(request, 'pmf/add_student.html')

def add_professor(request):
    return render(request, 'pmf/add_professor.html')

def list_students(request):
    students = Student.objects.all()
    return render(request, "pmf/student_list.html", {
        'not_empty': True,
        'students': students
    })

def list_professors(request):
    professors = Professor.objects.all()
    return render(request, "pmf/professor_list.html", {
        'not_empty': True,
        'professors': professors
    })