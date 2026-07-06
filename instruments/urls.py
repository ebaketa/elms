from django.urls import path
from . import views

urlpatterns = [
    path("", views.instrument_list, name="instrument_list"),
    path("new/", views.instrument_create, name="instrument_create"),
    path("<int:pk>/", views.instrument_detail, name="instrument_detail"),
    path("<int:pk>/edit/", views.instrument_edit, name="instrument_edit"),
    path("<int:pk>/delete/", views.instrument_delete, name="instrument_delete"),
]
