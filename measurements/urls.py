from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.measurement_list,
        name="measurement_list"
    ),

]