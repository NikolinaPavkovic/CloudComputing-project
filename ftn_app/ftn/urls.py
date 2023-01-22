from . import views
from django.urls import path

urlpatterns = [
    path('ftn/', views.index, name='options'),
    path('ftn/students/add', views.add_student, name='add-student'),
    path('ftn/professors/add', views.add_professor, name='add-professor'),
    path('ftn/students/list', views.list_students, name='list-students'),
    path('ftn/professors/list', views.list_professors, name='list-professors'),
]