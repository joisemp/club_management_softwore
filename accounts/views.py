from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegisterForm, CustomAuthenticationForm
from .models import OrgProfile


from accounts.verification_email import send_verification_mail
from django.utils.encoding import force_text
from . token_generator import account_activation_token
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse


from django.contrib.auth import views
from django.contrib.auth import login


class ProfilePageView(generic.TemplateView):
    template_name = 'accounts/profile.html'


class LoginView(views.LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('landing-page')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)
    

class LogoutView(views.LogoutView):
    template_name = 'accounts/logged_out.html'


class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.is_org = True
        user.save()
        OrgProfile.objects.create(user=user, name=form.cleaned_data['organisation_name'])
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
