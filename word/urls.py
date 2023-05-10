from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('', include('userapp.urls')),
    path('', include('mainapp.urls')),

]

"""  <<<<<<<< Keyinchalik o'qishim kerak >>>>>>

URL configuration for word project.

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

"""  <<<<<<<< Keyinchalik API ini chiqarishim kerak >>>>>>
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Word memorization API",
      default_version='v1',
      description="The most addictive learn to new word and spelling trivia quiz word game ever! It’s proven fact that learning new things in proper way helps you remember things quickly and for long-term! Word_Memorization is a new educational English memorizing a new word game that will check and improve your Vocabulary skills in an entertaining and challenging way!",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Ikromjon Ibrohimov: ikromjon7218@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)), """