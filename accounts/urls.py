from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('change-password/', login_required(views.ChangePasswordView.as_view()),
         name='change-password'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'),
    path('done-password-reset/', views.DonePasswordResetView.as_view(),
         name='done-password-reset'),
    path('confirm-password-reset/<uidb64>/<token>/',
         views.ConfirmPasswordResetView.as_view(), name='confirm-password-reset'),
    path('complete-password-reset/', views.CompletePasswordResetView.as_view(),
         name='complete-password-reset'),
    
    path('register-student/', views.StudentRegisterView.as_view(), name='register-student'),
    path('profile/', views.StudentProfileView.as_view(), name='profile'),
]
