from django.shortcuts import render
from .models import Student, Professor
from django.http import HttpResponse, JsonResponse

import requests

from .serializers import StudentSerializer, ProfessorSerializer

from .forms import RegisterStudentForm, RegisterProfessorForm

# Create your views here.
def index(request):
    return render(request, 'pmf/index.html')

def add_student(request):
    try:
        if request.method == 'GET':
            form = RegisterStudentForm()
        else:
            form = RegisterStudentForm(request.POST, request.FILES)
            if form.is_valid():
                student_index = form.cleaned_data['index']
                student_firstname = form.cleaned_data['firstname']
                student_lastname = form.cleaned_data['lastname']
                student_email = form.cleaned_data['email']
                student_image = form.files['image']
                student = Student(None, student_index, student_firstname, student_lastname, student_email, student_image)
                student_json = JsonResponse(StudentSerializer(student).data)
                response = requests.post('http://uns-app:8080/uns-app/student', headers={
                    'Content-Type': 'application/json',
                    'Accept-Encoding': 'gzip,deflate,br',
                    'Connection': 'keep-alive'
                }, data=student_json)
                if response.text != 'OK':
                    return HttpResponse('Student already exists.')
                else:
                    student = Student.objects.create(index=student_index, firstname=student_firstname, lastname=student_lastname, email=student_email, image=student_image)
                    student.save()
                    return HttpResponse('Student saved.')
    except Exception as exc:
        return HttpResponse(exc.__str__)

    return render(request, 'pmf/add_student.html', {
        'form': form
    })

def add_professor(request):
    try:
        if request.method == 'GET':
            form = RegisterProfessorForm()
        else:
            form = RegisterProfessorForm(request.POST, request.FILES)
            if form.is_valid():
                professor_firstname = form.cleaned_data['firstname']
                professor_lastname = form.cleaned_data['lastname']
                professor_email = form.cleaned_data['email']
                professor_image = form.files['image']
                professor = Professor(None, professor_firstname, professor_lastname, professor_email)
                professor_json = JsonResponse(ProfessorSerializer(professor).data)
                response = requests.post('http://uns-app:8080/uns-app/professor', headers={
                    'Content-Type': 'application/json',
                    'Accept-Encoding': 'gzip,deflate,br',
                    'Connection': 'keep-alive'
                }, data=professor_json)
                if response.text != 'OK':
                    return HttpResponse('Professor already exists.')
                else:
                    professor = Professor.objects.create(firstname=professor_firstname, lastname=professor_lastname, email=professor_email, image=professor_image)
                    professor.save()
                    return HttpResponse('Professor saved.')
    except Exception as exc:
        return HttpResponse(exc.__str__)
    return render(request, 'pmf/add_professor.html', {
        'form': form
    })

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