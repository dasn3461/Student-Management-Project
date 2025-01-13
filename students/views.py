from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomUserForm,ClassForm,StudentForm,TeacherForm,EnrollmentForm,GradeForm,AttendanceForm
from django.contrib.auth import authenticate,login,logout
from .models import Class, Student, Teacher, Enrollment, Grade, Attendance


# Create your views here.
def home(request):
   return render(request, 'students/home.html')


# Class Item

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})

def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'classes/class_form.html', {'form': form})

def class_detail(request, pk):
    class_instance = Class.objects.get(pk=pk)
    return render(request, 'classes/class_detail.html', {'class': class_instance})



# Student Item 

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


# Teacher Item

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher/teacher_form.html', {'form': form})

def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'teacher/teacher_detail.html', {'teacher': teacher})

# Enrolment Type

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment/enrollment_list.html', {'enrollments': enrollments})

def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment/enrollment_form.html', {'form': form})



# Grade Type

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade/grade_list.html', {'grades': grades}) 

def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'grade/grade_form.html', {'form': form})



# Attendance Type
def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendance_records': attendance_records})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/attendance_form.html', {'form': form})


# Registration View

def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration success you can login now!')
            return redirect('/login')
    return render(request, 'students/register.html', {'form':form})


# Login View

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            unm=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request, username=unm,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request, "Logged in Successfully!!")
                return redirect("/")
            else:
                messages.error(request, 'Invalid username and Password!!')
                return redirect('/login')
        return render(request, 'students/login.html')


# Logout View
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Loggedout Successfully !!')
    return redirect("/")
















