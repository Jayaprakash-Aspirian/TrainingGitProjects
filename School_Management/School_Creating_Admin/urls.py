from django.urls import path
from School_Creating_Admin import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("register/", views.signup, name="signup"),
    path("addusers/", views.addusers, name="addusers"),
    path("login/", views.login, name="login"),
    path("login/authenticate_user/", views.authenticate_user, name="authenticate_user"),
    path("main_admin_dashboard/",views.main_admin_dashboard,name="main_admin_dashboard"),
    path("main_admin_logout/", views.main_admin_logout, name="main_admin_logout"),
    path("create_school_admin/",views.create_school_admin,name="create_school_admin"),
    path("addschool/", views.addschool, name="addschool"),
]