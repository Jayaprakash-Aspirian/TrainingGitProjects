from School_Creating_Admin.models import school_details
from .form import SchoolAdminRegistrationForm, UserRegistrationForm, UserLoginForm
from django.shortcuts import render, redirect
from School_Creating_Admin.models import MyUser
from django.shortcuts import render, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def signup(request):
    title = "Admin Registration"
    users = UserRegistrationForm()
    return render(request, "signup.html", {"form": users, "title": title})


def addusers(request):
    users = UserRegistrationForm(request.POST)
    if request.method == "POST":
        if users.is_valid():
            username = users.cleaned_data["username"]
            firstname = users.cleaned_data["firstname"]
            lastname = users.cleaned_data["lastname"]
            email = users.cleaned_data["email"]
            password = users.cleaned_data["password"]
            # username validation
            if MyUser.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return render(request, "signup.html", {"form": users})
            # email id validation
            elif MyUser.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return render(request, "signup.html", {"form": users})
            else:
                # add users in user model
                userInf = MyUser.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password,
                )
                group = Group.objects.get(name="Product_Admin")
                userInf.groups.add(group)
                userInf.save()
               
                messages.info(
                    request,
                    "User Created!!! Login Here...",
                    extra_tags="correct_message",
                )
                return redirect("login")
        else:
            return render(request, "signup.html", {"form": users})
    else:
        messages.info(request, "Invalid inputs")
        return render(request, "signup.html", {"form": users})


def login(request):
    title="Admin Login"
    form = UserLoginForm()
    return render(request, "login.html", {"form": form,"title":title})


def authenticate_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check user or not
        user = auth.authenticate(username=username, password=password)
        if user is not None and (
            user.groups.filter(name="Product_Admin")
        ):
            auth.login(request, user)
            messages.info(request, "Successfully logged in..!!")
            return redirect("main_admin_dashboard")
        else:
            messages.info(request, "Invalid Login")
            return redirect("login")
    else:
        messages.info(request, "Not a post request!!!")

def main_admin_dashboard(request):
    schools=school_details.objects.all()
    users=MyUser.objects.all()
    return render(request,"main_admin_dashboard.html",{"schools":schools,"users":users})

def main_admin_logout(request):
    auth.logout(request)
    return redirect("login")

def create_school_admin(request):
    form=SchoolAdminRegistrationForm()
    schools=school_details.objects.all()
    return render(request,"create_school_admin.html",{"form":form,"schools":schools})

def addschool(request):
    form=SchoolAdminRegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid() :
            schoolname = form.cleaned_data["schoolname"]
            schooladdress = form.cleaned_data["schooladdress"]
            schooldistrict= form.cleaned_data["schooldistrict"]
            username=form.cleaned_data["username"]
            password =form.cleaned_data["password"]
            # username validation
            if MyUser.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return render(request,"create_school_admin.html",{"form":form})
            else:
                # add users in user model
                userInf = MyUser.objects.create_user(
                    username=username,
                    password=password,
                )
                group = Group.objects.get(name="School_Admin")
                userInf.groups.add(group)
                userInf.save()
                schooldetail = school_details.objects.create(
                    schoolname = schoolname,
                    schooladdress = schooladdress,
                    schooldistrict = schooldistrict,
                    user_id=userInf.id,
                )
                schooldetail.save()

                messages.info(
                    request,
                    "School is Created!!!...",
                    extra_tags="correct_message",
                )
                return redirect("login")
        else:
           return render(request,"create_school_admin.html",{"form":form})
    else:
        messages.info(request, "Invalid inputs")
        return render(request,"create_school_admin.html",{"form":form})