"""jeo_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, include
from rest_framework import routers

from jeo_services.views.provider import ProviderViewSet
from jeo_services.views.service_area import ServiceAreaViewSet


router = routers.DefaultRouter()
router.register(r'providers', ProviderViewSet, basename='providers')
router.register(r'service_areas', ServiceAreaViewSet, basename='service_areas')


urlpatterns = [
    path('/api/v1/', include(router.urls)),
]
