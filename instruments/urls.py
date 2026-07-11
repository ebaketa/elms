from django.urls import path
from . import views

urlpatterns = [

    path("", views.instrument_list, name="instrument_list"),

    path("create/", views.instrument_create, name="instrument_create"),

    path("<int:pk>/", views.instrument_detail, name="instrument_detail"),

    path("<int:pk>/edit/", views.instrument_edit, name="instrument_edit"),

    path("<int:pk>/delete/", views.instrument_delete, name="instrument_delete"),

    path("<int:pk>/connect/", views.instrument_connect, name="instrument_connect"),

    path("<int:pk>/identify/", views.instrument_identify, name="instrument_identify"),

    path("<int:pk>/measure/", views.instrument_measure, name="instrument_measure"),

]