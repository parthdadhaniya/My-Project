"""doctortracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.RegistrationPage,name="registration"),
    path('login/',views.LoginPage,name="login"),
    path('registeruser/',views.RegisterUser, name="registeruser"),
    path('login_evealuate/',views.login_evaluation,name="login-evaluate"),
    path('forgotpassword/' ,views.forgotPage,name="forgot"),
    path('verify-otp-password/',views.forgotPassword,name="forgot-password"),
    path('logout/',views.logout,name="logout"),
    path('homepage/',views.Homepage,name="homepage"),
    path('reset-password/',views.ResetPassword,name="reset-password"),
    path('all-patient/',views.PatientList,name="patient-list"),
    path('edit-patient-profile/',views.EditPatientprofile,name="edit-patient-profile"),
    path('doctor-profile-picture/',views.DoctorProfilePicture,name="doctor-profile-picture"),
    path('',views.IndexPage,name="index"),
    path('add-patient',views.AddPatient,name="add-patient"),
    path('add-new-case',views.AddNewCase,name="add-new-case"),
    path('get-patient-details/',views.GetPatientDetails,name="get-patient-details"),
    path('create-new-case/',views.AddNewCaseToDatabase,name="create-new-case"),
    path('all-case/',views.allcase,name="allcase"),

]


