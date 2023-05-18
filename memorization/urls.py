from django.urls import path
from .views import *


urlpatterns = [
    path("query_memorization/", query_memorization),
    path("test_memorization/", test_memorization),

]