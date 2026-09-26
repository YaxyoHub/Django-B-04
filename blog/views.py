from django.shortcuts import render, redirect
from .models import Student
from .forms import Student_Form
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home_view(request):
    user = request.user.pk
    print(user)
    return render(
        request,
        'index.html'
    )

@login_required(login_url='login')
def about_view(request):
    return render(
        request,
        'about.html'
    )

@login_required(login_url='login')
def students_view(request):
    students = Student.objects.all()

    for i in students:
        print(i.image.url)
        
    return render(
        request,
        'students.html',
        context={
            'students': students
        }
    )

@login_required(login_url='login')
def detailt_student_view(request, id):
    student = Student.objects.get(pk=id)
    return render(
        request,
        'detail_student.html',
        context={
            'student': student
        }
    )

@login_required(login_url='login')
def edit_student_view(request, id):
    student = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = Student_Form(request.POST, request.FILES, instance=student)
        form.save()
        return redirect('students')

    edit_form = Student_Form(instance=student)
    return render(
        request,
        'edit_student.html',
        context={'form': edit_form}
    )

@login_required(login_url='login')
def delete_student_view(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('students')

@login_required(login_url='login')
def create_student_view(request):
    if request.method == 'POST':
        form = Student_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')

    empty_form = Student_Form()
    return render(
        request,
        'create_student.html',
        context={'form': empty_form}
    )

# shop

# contact

# news


