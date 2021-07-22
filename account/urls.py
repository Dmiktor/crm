from django.urls import path
from . import views

urlpatterns = [
    path('log_in', views.login_in, name='login_in'),
    path('log_out', views.login_out, name='login_out'),
]
