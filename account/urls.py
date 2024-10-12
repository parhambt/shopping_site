from django.urls import path
from . import views

urlpatterns=[ path("register/",views.Register.as_view(),name="register"),
             path("login/",views.login,name="login"),
             path("logout/",views.logout,name="logout"),
             path("activate/<uidb64>/<token>/",views.activate , name='activate'),
             path("dashboard/",views.dashboard , name="dashboard"),
             path("",views.dashboard ,name="dashboard" ),
             path("forgotpassword/",views.forget_pass,name="forgotpassword"),
             path("reset_passwrod_validate/<uidb64>/<token>/",views.reset_passwrod_validate , name='reset_passwrod_validate'),
             path("resetpassword/",views.ResetPassword.as_view(),name="resetpassword"),
             path("edit_profile/" , views.edit_profile , name="edit_profile"),
             path("change_password/",views.change_password , name="change_password"),



]