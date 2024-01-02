from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="find_all"),
    path("/<int:id>", views.get_by_id, name="find_all"),
]