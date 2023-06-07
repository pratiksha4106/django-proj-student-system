from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentForm
# Create your views here.

def home(request):
    return render(request,'home.html',{
        'student':Student.objects.all()
    })

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_stud_Id = form.cleaned_data['Student_ID']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_perc = form.cleaned_data['percentage']

            new_student = Student(
                Student_ID = new_stud_Id,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                percentage = new_perc
            )
            new_student.save()
            return render(request,'add.html',{
                'form':StudentForm(),
                'success':True
            })
    else:
        form = StudentForm()
    return render(request,'add.html',{
        'form':StudentForm()
    })   
            
