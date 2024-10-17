#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def home_view(request):
    return render(request, 'home.html')

def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
