from django.urls import path
from .import views

app_name = 'clubs'


urlpatterns = [
    path("", views.clubs_list, name="club-list"),
    path("create", views.club_create_view, name="club-create"),
    path("<id>", views.club_detail_view, name="club-detail"),
    path("<id>/edit", views.club_edit_view, name="club-edit"),
    path("<id>/delete", views.club_delete_view, name="club-delete"),
]
