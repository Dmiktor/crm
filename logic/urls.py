from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/<str:cat>', views.events_by_category, name='events_list_by_category'),
    path('participants/', views.partner_list, name='partner_list'),
    path('workers/', views.workers_list, name='workers_list'),
    path('recipient_of_services/', views.recipientservices_list, name='servisetaker_list'),
    path('service_providers/', views.serviceprovider_list, name='servisegiver_list'),
    path('participants/detailed/<str:name>', views.partner_detailed, name='partner_detailed'),
    path('participants/detailed/<str:name>/add_action', views.action_profile_add, name='action_profile_new'),
    path('services/', views.service_list, name='service_list'),
    path('services/detailed/<str:title>', views.service_detailed, name='service_detailed'),
    path('project/<str:cat>', views.projects_list_by_category, name='projects_list_by_category'),
]
