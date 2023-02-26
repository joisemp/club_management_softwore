from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

app_name = 'org'


urlpatterns = [
    path('profile/', login_required(views.OrgProfilePageView.as_view()), name='org-profile'),
]
