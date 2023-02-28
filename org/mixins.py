from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrgOnlyAccessMixin(AccessMixin):
    """Verify that the current user is authenticated and is organisor."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_org:
            return redirect('landing-page')
        return super().dispatch(request, *args, **kwargs)