from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('treat',views.treat),
    path('trainer',views.trainer),
    path('chat',views.chat),
    path('info',views.info)
]
