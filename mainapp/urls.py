from django.urls import path
from .views import *

urlpatterns = [
    path('home_page/', home_page),
    path('4000_essential_english_words/', essential_english_words),
    path('error/', error),
    path('settings/', settings),
    path('about/', about),

    path('query_essential_1/', query_essential_1),
    path('test_1_essential/', test_1_essential),
    path('result/', result)

]
# 1) gapda tushib qolgan so'z ni topish kerak.
# 2) gap beriladi, unga ma'no jihatdan yaqin so'z.
