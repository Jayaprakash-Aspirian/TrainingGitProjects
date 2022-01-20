from django.urls import path
from School_Admin_App import views

urlpatterns = [
    path("login/", views.login, name="school_admin_login"),
    path("login/authenticate_schooladmin/", views.authenticate_schooladmin, name="authenticate_schooladmin"),
    path("school_admin_dashboard/", views.school_admin_dashboard, name="school_admin_dashboard"),

    path("create_teacher_account/",views.create_teacher_account,name="create_teacher_account"),
    path('create_student_account/',views.create_student_account,name="create_student_account"),
    path('create_student_subjects/',views.create_student_subjects,name="create_student_subjects"),

    path("addteacher/",views.addteacher,name="addteacher"),
    path("addsubjects/",views.addsubjects,name="addsubjects"),
    path("teacher_login/", views.teacher_login, name="teacher_login"),
    path("teacher_login/authenticate_teacher/", views.authenticate_teacher, name="authenticate_teacher"),
    path("student_login/", views.student_login, name="student_login"),
    path("student_login/authenticate_student/", views.authenticate_student, name="authenticate_student"),
    
    path("school_admin_logout/", views.school_admin_logout, name="school_admin_logout"),
    path("teacher_logout/", views.teacher_logout, name="teacher_logout"),
    path("student_logout/", views.student_logout, name="student_logout"),
]