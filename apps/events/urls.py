from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_list, name='events'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('registration/<int:event_id>/', views.event_registration, name='event_registration'),
    path('ajax/filter/', views.events_ajax_filter, name='events_ajax_filter'),
] 