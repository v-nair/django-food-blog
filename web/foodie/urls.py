"""
URL configuration for foodie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django_prometheus import exports
from .views import health_view, home_view
from django.conf import settings
from django.conf.urls.static import static
from manager import views as admin_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("metrics/", exports.ExportToDjangoView, name="metrics"), # Prometheus metrics endpoint
    path("health/", health_view, name="health"), # Health check endpoint
    path('', home_view, name='home'),  # default page
    path("menu/", include('menu.urls')), # connected to menu
    path("register/", admin_views.register, name="register"), # connected to menu
    path("login/", auth_views.LoginView.as_view(template_name='manager/login.html'), name="login"), # default redirect is to accounts/profile
    path("logout/", auth_views.LogoutView.as_view(template_name='manager/logout.html'), name="logout"),
    path("profile/", admin_views.profile, name="profile"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

