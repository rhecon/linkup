
from django.urls import path
from . import views


urlpatterns = [
    path("meetups/", views.home, name="all-meetups"),
    path("meetups/registration-success", views.confirm_registration, name="registration-confirmation"),
    # slug converter tells django that the dynamic value we have in meetup_slug shoud match the slug format
    path("meetup-detail/<slug:meetup_slug>", views.meetup_details, name="meetup-detail"),
]
