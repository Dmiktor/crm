from django.urls import path
from . import views

urlpatterns = [
    path('log_in', views.login_in, name='login_in'),
    path('log_out', views.login_out, name='login_out'),
    path('my_page', views.my_page, name='my_page'),
    path('my_expertise_requests', views.expertise_requests, name='my_expertise_requests'),
]
