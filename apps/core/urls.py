from django.urls import path
from . import views

urlpatterns = [
    # Основні сторінки
    path('', views.HomeView.as_view(), name='home'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('calculator/', views.CalculatorView.as_view(), name='calculator'),
    path('developer/', views.DeveloperView.as_view(), name='developer'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    
    # AJAX обробка форм
    path('forms/submit/', views.handle_form_submission, name='form_submit'),
    path('forms/test/', views.handle_test_submission, name='test_submit'),
] 