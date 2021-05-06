from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("admin/advisor", views.add_advisor, name="add_advisor"),
    path("contact/<int:year>/", views.contact1, name="contact"),
    path("contact/", views.contact, name="contact")
]
