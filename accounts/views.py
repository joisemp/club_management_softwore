from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import StudentProfileForm, UserRegisterForm, CustomAuthenticationForm
from .models import StudentProfile
from org.models import OrgProfile
from .mixins import CheckUserAndRedirectMixin
from accounts.verification_email import send_verification_mail
from django.utils.encoding import force_text
from . token_generator import account_activation_token
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.contrib.auth import views
from django.contrib.auth import login
from .uitils import generate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class LandingPageView(CheckUserAndRedirectMixin, generic.TemplateView):
    template_name = 'landing_page.html'


class LoginView(CheckUserAndRedirectMixin, views.LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return redirect('landing-page')


class LogoutView(views.LogoutView):
    template_name = 'accounts/logged_out.html'


class UserRegisterView(CheckUserAndRedirectMixin, generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.is_org = True
        user.save()
        OrgProfile.objects.create(
            user=user, name=form.cleaned_data['organisation_name'])
        send_verification_mail(self.request, user, form)
        return super(UserRegisterView, self).form_valid(form)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    elif user is not None and user.is_active:
        return redirect('accounts:login')
    else:
        return HttpResponse('Activation link is invalid!')


class ChangePasswordView(views.PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('landing-page')


class ResetPasswordView(views.PasswordResetView):
    email_template_name = 'accounts/password_reset/password_reset_email.html'
    html_email_template_name = 'accounts/password_reset/password_reset_email.html'
    subject_template_name = 'accounts/password_reset/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:done-password-reset')
    template_name = 'accounts/password_reset/password_reset_form.html'


class DonePasswordResetView(views.PasswordResetDoneView):
    template_name = 'accounts/password_reset/password_reset_done.html'


class ConfirmPasswordResetView(views.PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:complete-password-reset')
    template_name = 'accounts/password_reset/password_reset_confirm.html'


class CompletePasswordResetView(views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset/password_reset_complete.html'


class StudentRegisterView(generic.CreateView):
    form_class = StudentProfileForm
    template_name = 'accounts/register_student.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = str(generate_password())
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        
        user = User.objects.create(
            email = email,
            password = password,
            is_student = True
        )
        user.save()
        
        student_profile = StudentProfile.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            org = OrgProfile.objects.get(user=self.request.user),
            user = user
        )
        student_profile.save()
        return redirect('org:student-list')


class StudentProfileView(generic.TemplateView):
    template_name = 'accounts/profile.html'
