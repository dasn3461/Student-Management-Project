from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/', views.login_page,name="login"),
    path('logout/', views.logout_page,name="logout"),
    
    # Classes Urls
    path('classes/', views.class_list, name='class_list'),
    path('class/create/', views.class_create, name='class_create'),
    path('class/<int:pk>/', views.class_detail, name='class_detail'),
    
    # Students Urls
    path('students/', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    
    # Teachers Urls
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/create/', views.teacher_create, name='teacher_create'),
    path('teacher/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    
    # Enrollments Urls
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollment/create/', views.enrollment_create, name='enrollment_create'),
    
    # Grades Urls
    path('grades/', views.grade_list, name='grade_list'),
    path('grade/create/', views.grade_create, name='grade_create'),
    
    # Attendance Urls
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),


  

    
]






   

