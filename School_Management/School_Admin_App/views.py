from School_Creating_Admin.form import  UserLoginForm,UserRegistrationForm
from django.shortcuts import render, redirect
from School_Creating_Admin.models import MyUser
from django.shortcuts import render, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from School_Creating_Admin.models import school_details
from School_Admin_App.form import TeacherRegistrationForm,ClassSubjectsForm
from School_Admin_App.models import Teacher_Details,Class_Subjects,Student_Details,Student_Subjects_Marks


def login(request):
    title="School Admin Login"
    action="authenticate_schooladmin/"
    form = UserLoginForm()
    return render(request, "school_admin_login.html", {"form": form,"title":title,"action":action})


def authenticate_schooladmin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check user or not
        user = auth.authenticate(username=username, password=password)
        
        if user is not None and (
            user.groups.filter(name="School_Admin")
        ):
            auth.login(request, user)
            messages.info(request, "Successfully logged in..!!")
            return redirect("school_admin_dashboard")
        else:
            messages.info(request, "Invalid Login")
            return redirect("school_admin_login")
    else:
        messages.info(request, "Not a post request!!!")

def school_admin_dashboard(request):
    teachers=Teacher_Details.objects.all()
    user = auth.get_user(request)
    school=school_details.objects.all()
    teacherclass=Teacher_Details.objects.filter(user_id=request.user.id)
    if user.groups.filter(name='School_Admin').exists() :
        school=get_object_or_404(school_details, user_id=request.user.id)
    elif user.groups.filter(name='Teacher').exists()  :
        teacherclass=get_object_or_404(Teacher_Details, user_id=request.user.id)
        
    
    return render(request, "school_admin_dashboard.html",{"teachers":teachers,"teacherclass":teacherclass,"school":school})

def create_teacher_account(request):
    form=TeacherRegistrationForm()
    form1=UserRegistrationForm
    teachers=Teacher_Details.objects.all()
    user = auth.get_user(request)
   
    if user.groups.filter(name='School_Admin').exists():
        school=get_object_or_404(school_details, user_id=request.user.id)
    else:
        school=school_details.objects.all()
    return render(request,"create_teacher_account.html",{"form":form,"form1":form1,"teachers":teachers,"school":school})


def create_student_account(request):
    return render(request, "create_student_account.html")

def create_student_subjects(request):
    form=ClassSubjectsForm()
    return render(request, "create_student_subjects.html",{"form":form})

def addsubjects(request):
    form=ClassSubjectsForm(request.POST)
    print(request.user.id)
    if request.method == "POST":
        if form.is_valid() :
            class_is=form.cleaned_data["class_is"]
            first_subject = form.cleaned_data["first_subject"]
            second_subject = form.cleaned_data["second_subject"]
            third_subject= form.cleaned_data["third_subject"]
            fourth_subject=form.cleaned_data["fourth_subject"]
            fifth_subject =form.cleaned_data["fifth_subject"]
            sixth_subject =form.cleaned_data["sixth_subject"]
            userInf=get_object_or_404(school_details,user_id=request.user.id)
            if Class_Subjects.objects.filter(school_id=userInf.id,class_is=class_is).exists():
                ClassSubject_is=get_object_or_404(Class_Subjects,class_is=class_is)
                ClassSubject_is.first_subject=first_subject
                ClassSubject_is.second_subject=second_subject
                ClassSubject_is.third_subject=third_subject
                ClassSubject_is.fourth_subject=fourth_subject
                ClassSubject_is.fifth_subject= fifth_subject
                ClassSubject_is.sixth_subject=sixth_subject
                ClassSubject_is.save()
            else:
                ClassSubjects=Class_Subjects.objects.create(
                    school_id=userInf.id,
                    class_is=class_is,
                    first_subject=first_subject,
                    second_subject=second_subject,
                    third_subject=third_subject,
                    fourth_subject=fourth_subject,
                    fifth_subject=fifth_subject,
                    sixth_subject =sixth_subject,
                
                )
                ClassSubjects.save()
            
            return render(request,"create_student_subjects.html",{"form":form})
        else:
           return render(request,"create_student_subjects.html",{"form":form})
    else:
        messages.info(request, "Invalid inputs")
        return render(request,"create_student_subjects.html",{"form":form})



def addteacher(request):
    form=TeacherRegistrationForm(request.POST)
    form1=UserRegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid() and form1.is_valid() :
            username = form1.cleaned_data["username"]
            firstname = form1.cleaned_data["firstname"]
            lastname = form1.cleaned_data["lastname"]
            email = form1.cleaned_data["email"]
            password = form1.cleaned_data["password"]
            teacher_subject=form.cleaned_data["teacher_subject"]
            teacher_address=form.cleaned_data["teacher_address"]
            teacher_phone=form.cleaned_data["teacher_phone"]

            teacher_taking_class1=form.cleaned_data["teacher_taking_class1"]
            teacher_taking_class2=form.cleaned_data["teacher_taking_class2"]
            teacher_taking_class3=form.cleaned_data["teacher_taking_class3"]
            teacher_taking_class4=form.cleaned_data["teacher_taking_class4"]
            teacher_taking_class5=form.cleaned_data["teacher_taking_class5"]
            teacher_taking_class1_section=form.cleaned_data["teacher_taking_class1"]
            teacher_taking_class2_section=form.cleaned_data["teacher_taking_class2"]
            teacher_taking_class3_section=form.cleaned_data["teacher_taking_class3"]
            teacher_taking_class4_section=form.cleaned_data["teacher_taking_class4"]
            teacher_taking_class5_section=form.cleaned_data["teacher_taking_class5"]


            # username validation
            if MyUser.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return render(request,"create_teacher_account.html",{"form":form,"form1":form1})
            elif MyUser.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return render(request,"create_teacher_account.html",{"form":form,"form1":form1})
            else:
                # add users in user model
                userInf = MyUser.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password,
                )
                group = Group.objects.get(name="Teacher")
                userInf.groups.add(group)
                userInf.save()
                teacherdetails = Teacher_Details.objects.create(
                    teacher_subject=teacher_subject,
                    teacher_address=teacher_address,
                    teacher_phone=teacher_phone,
                    teacher_taking_class1=teacher_taking_class1,
                    teacher_taking_class2=teacher_taking_class2,
                    teacher_taking_class3=teacher_taking_class3,
                    teacher_taking_class4=teacher_taking_class4,
                    teacher_taking_class5=teacher_taking_class5,
                    teacher_taking_class1_section=teacher_taking_class1_section,
                    teacher_taking_class2_section=teacher_taking_class2_section,
                    teacher_taking_class3_section=teacher_taking_class3_section,
                    teacher_taking_class4_section=teacher_taking_class4_section,
                    teacher_taking_class5_section=teacher_taking_class5_section,

                    user_id=userInf.id,

                )

                
                teacherdetails.save()

                messages.info(
                    request,
                    "teacher account is Created!!!...",
                    extra_tags="correct_message",
                )
                return render(request,"create_teacher_account.html",{"form":form,"form1":form1})
        else:
           return render(request,"create_teacher_account.html",{"form":form,"form1":form1})

    else:
        messages.info(request, "Invalid inputs")
        return render(request,"create_teacher_account.html",{"form":form,"form1":form1})


def teacher_login(request):
    title="Teacher Login"
    form = UserLoginForm()
    action="authenticate_teacher/"
    return render(request, "school_admin_login.html", {"form": form,"title":title,"action":action})



def authenticate_teacher(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check user or not
        user = auth.authenticate(username=username, password=password)
        
        if user is not None and (
            user.groups.filter(name="Teacher")
        ):
            auth.login(request, user)
            messages.info(request, "Successfully logged in..!!")
            return redirect("school_admin_dashboard")
        else:
            messages.info(request, "Invalid Login")
            return redirect("school_admin_login")
      
    else:   
        messages.info(request, "Not a post request!!!")

def student_login(request):
    title="Student Login"
    form = UserLoginForm()
    action="authenticate_student/"
    return render(request, "school_admin_login.html", {"form": form,"title":title,"action":action})



def authenticate_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check user or not
        user = auth.authenticate(username=username, password=password)
        
        if user is not None and (
            user.groups.filter(name="Student")
        ):
            auth.login(request, user)
            messages.info(request, "Successfully logged in..!!")
            return redirect("school_admin_dashboard")
        else:
            messages.info(request, "Invalid Login")
            return redirect("school_admin_login")

    else:   
        messages.info(request, "Not a post request!!!")


def school_admin_logout(request):
    auth.logout(request)
    return redirect("school_admin_login")

def teacher_logout(request):
    auth.logout(request)
    return redirect("teacher_login")

def student_logout(request):
    auth.logout(request)
    return redirect("student_login")
