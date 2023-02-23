from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrgOnlyAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is organisor."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_org:
            return redirect('landing-page')
        return super().dispatch(request, *args, **kwargs)


class CheckUserAndRedirectMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_org:
                return redirect('accounts:org-profile')
            else:
                return redirect('clubs:club-list')
        return super().dispatch(request, *args, **kwargs)
