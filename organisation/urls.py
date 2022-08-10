from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

app_name = 'organisation'

urlpatterns = [
    path('dashboard/', views.OrgDashboardView.as_view(), name='org-dashboard'),
]
