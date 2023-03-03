from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

app_name = 'org'


urlpatterns = [
    path('', login_required(views.OrgDashboardView.as_view()), name='dashboard'),
    path('profile/', login_required(views.OrgProfilePageView.as_view()), name='profile'),
    path('students/', login_required(views.StudentListView.as_view()), name='student-list'),
    path("<id>/edit", views.student_edit_view, name="student-edit"),
    path("<id>/delete", views.student_delete_view, name="student-delete"),
]
