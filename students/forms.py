from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student, Teacher, Enrollment,Class,Grade,Attendance


class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter confirm password'}))
    
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']  




class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter class name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter class description', 'rows': 3}),
        }
        
        



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'roll_number', 'student_class']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter student age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter student email'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter roll number'}),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
            
        }
        
        



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'phone', 'assigned_class']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned_class': forms.Select(attrs={'class': 'form-control'}),
            
        }
        
        


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'student_class']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
        }
      
      


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

      

        
      
        
        
        
        




        
        
        
        


        