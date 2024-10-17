from django.urls import path
from .views import student_create_view, student_list_view, home_view

urlpatterns = [
    
    path('home/',home_view,name='homeview'),
    path('add/', student_create_view, name='student_add'),
    path('list/', student_list_view, name='student_list'),
]
