from django.db import models

# Model for Class
class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name

# Model for Student
class Student(models.Model):
    name = models.CharField(max_length=100)  
    age = models.PositiveIntegerField()  
    email = models.EmailField(unique=True)  
    roll_number = models.CharField(max_length=10, unique=True)  
    student_class = models.ForeignKey(Class, related_name='students', on_delete=models.CASCADE)  
    enrollment_date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

# Model for Teacher
class Teacher(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15, blank=True, null=True)  
    assigned_class = models.ForeignKey(Class, related_name='teachers', on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.name

# Model for Enrollment
class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.student_class.name}"

# Model for Grade 
class Grade(models.Model):
    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100) 
    grade = models.CharField(max_length=2)  
    date_assigned = models.DateField(auto_now_add=True)  

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.grade}"

# Model for Attendance
class Attendance(models.Model):
    student = models.ForeignKey(Student, related_name='attendance_records', on_delete=models.CASCADE)
    date = models.DateField()  
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])  

    def __str__(self):
        return f"{self.student.name} - {self.status} on {self.date}"
