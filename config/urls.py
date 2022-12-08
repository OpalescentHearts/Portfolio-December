from django.contrib import admin
from django.urls import path
from app import views
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("aboutme/", views.about),
    path("projects", views.projects),
    path("skills", views.skills),
]
