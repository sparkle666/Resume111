from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "index"),
    path("skills/", add_skills, name = "add_skills"),
]
