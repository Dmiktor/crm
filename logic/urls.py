from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('partner_register', views.partner_register, name='partner_register'),
    path('partner_register/<str:indef>/cont', views.partner_register_cont, name='partner_register_cont'),
    path('partner_register/<str:indef>/last', views.partner_register_last, name='partner_register_last'),
    path('events/<str:cat>', views.events_by_category, name='events_list_by_category'),
    path('participants/', views.partner_list, name='partner_list'),
    path('workers/', views.workers_list, name='workers_list'),
    path('recipient_of_services/', views.recipientservices_list, name='servisetaker_list'),
    path('service_providers/', views.serviceprovider_list, name='servisegiver_list'),
    path('participants/detailed/<str:indef>', views.partner_detailed, name='partner_detailed'),
    path('participants/detailed/<str:indef>/add_action', views.action_profile_add, name='action_profile_new'),
    path('services/', views.service_list, name='service_list'),
    path('services/detailed/<str:title>', views.service_detailed, name='service_detailed'),
    path('development/', views.development_list, name='development_list'),
    path('development/take_by_me+<int:pk>', views.development_take, name='development_take'),
    path('my_projects/', views.my_projects, name='my_projects'),
    path('my_projects/detailed/<int:pk>', views.project_detailed, name='project_detailed'),

]
