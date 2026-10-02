"""
URL configuration for linkup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    # If we enter our domain without passing any arguements it redirects to meetups
    # This automatatically takes us to the meetups page, instead of us manually entering /meetups when loading the page
    path("", RedirectView.as_view(url="/meetups")),
    path("meetups/", include("meetup.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
