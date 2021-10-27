"""ExpertAutoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from appraisal import views as appraisal_views
from django.contrib.auth import views as auth_views
from appraisal.forms import UserLoginForm
from appraisal.views import ( VehicleCreateView, VehicleDetailView, VehicleListView, VehicleUpdateView )
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", appraisal_views.home),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/login.html"), name='logout'),
    path("register/", appraisal_views.register, name="register"),
    path("", include('appraisal.urls'))    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
