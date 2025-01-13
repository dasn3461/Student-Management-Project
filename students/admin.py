from django.contrib import admin
from .models import Student, Teacher, Class, Enrollment, Grade, Attendance

# Register Class model using the decorator
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

# Register Teacher model using the decorator
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'assigned_class')
    search_fields = ('name', 'email')
    list_filter = ('assigned_class',)

# Register Student model using the decorator
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'student_class', 'age', 'email', 'enrollment_date')
    search_fields = ('name', 'roll_number', 'email')
    list_filter = ('student_class',)

# Register Enrollment model using the decorator
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'student_class', 'enrollment_date')
    search_fields = ('student__name', 'student_class__name')
    list_filter = ('student_class',)

# Register Grade model using the decorator
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'date_assigned')
    search_fields = ('student__name', 'subject')
    list_filter = ('subject',)

# Register Attendance model using the decorator
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    search_fields = ('student__name', 'date')
    list_filter = ('status',)
