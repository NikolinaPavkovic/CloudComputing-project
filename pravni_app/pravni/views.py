from django.shortcuts import render
from .models import Student, Professor

# Create your views here.
def index(request):
    return render(request, 'pravni/index.html')

def add_student(request):
    return render(request, 'pravni/add_student.html')

def add_professor(request):
    return render(request, 'pravni/add_professor.html')

def list_students(request):
    students = Student.objects.all()
    return render(request, "pravni/student_list.html", {
        'not_empty': True,
        'students': students
    })

def list_professors(request):
    professors = Professor.objects.all()
    return render(request, "pravni/professor_list.html", {
        'not_empty': True,
        'professors': professors
    })
