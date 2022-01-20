from django.contrib import admin
from School_Admin_App.models import Teacher_Details,Student_Details,Student_Subjects_Marks,Class_Subjects
# Register your models here.

admin.site.register(Teacher_Details)
admin.site.register(Student_Details)
admin.site.register(Student_Subjects_Marks)
admin.site.register(Class_Subjects)