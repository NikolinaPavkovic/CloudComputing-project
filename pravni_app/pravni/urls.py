from . import views
from django.urls import path

urlpatterns = [
    path('pravni/', views.index, name='options'),
    path('pravni/students/add', views.add_student, name='add-student'),
    path('pravni/professors/add', views.add_professor, name='add-professor'),
    path('pravni/students/list', views.list_students, name='list-students'),
    path('pravni/professors/list', views.list_professors, name='list-professors'),
]