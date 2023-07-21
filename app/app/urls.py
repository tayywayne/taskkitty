from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_home(request):
    return redirect("show_my_tasks")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_home, name="home"),
    path("tasks/", include("tasks.urls")),
    path("users/", include("users.urls")),
]
