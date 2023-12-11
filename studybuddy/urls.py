from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("delete_audio/<int:audio_id>/",
         views.delete_audio, name="delete_audio"),
    path("generate_notes/<int:audio_id>/",
         views.generate_notes, name="generate_notes"),
    path("view_note/<int:note_id>/", views.view_note, name="view_note"),
    path("rename_note/<int:note_id>/", views.rename_note, name="rename_note"),
    path("edit_note/<int:note_id>/", views.edit_note, name="edit_note"),
    path("delete_note/<int:note_id>/", views.delete_note, name="delete_note"),
]
