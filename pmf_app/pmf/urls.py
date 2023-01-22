from . import views
from django.urls import path

urlpatterns = [
    path('pmf/', views.index, name='options'),
    path('pmf/students/add', views.add_student, name='add-student'),
    path('pmf/professors/add', views.add_professor, name='add-professor'),
    path('pmf/students/list', views.list_students, name='list-students'),
    path('pmf/professors/list', views.list_professors, name='list-professors'),
]