from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class CheckUserAndRedirectMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_org:
                return redirect('org:dashboard')
            else:
                return redirect('accounts:profile')
        return super().dispatch(request, *args, **kwargs)
