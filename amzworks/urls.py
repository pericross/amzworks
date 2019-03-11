"""amzworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.authtoken import  views as drf_views
# from rest_framework import routers
# from drf import views

# router = routers.DefaultRouter()

# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Write up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    url(r'accounts/', include('users.urls')),
    path('app/', include('app.urls')),
#    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# path('', include(router.urls)),
