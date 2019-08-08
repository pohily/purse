"""purse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('', views.purse_app_start, name='purse_app_start'),

    path('purse_app/settings/', views.settings, name='settings'),
    path('purse_app/summary_settings/', views.summary_settings, name='summary_settings'),
    path('purse_app/purchase_bl/', views.purchase_bl, name='purchase_bl'),
    path('purse_app/income_bl/', views.income_bl, name='income_bl'),

    path('purse_app/purchase/', views.purchase, name='purchase'),
    path('purse_app/new_purchase/', views.new_purchase, name='new_purchase'),
    path('purse_app/purchase_edit/<int:pk>/', views.purchase_edit, name='purchase_edit'),
    path('purse_app/purchase_remove/<int:pk>/', views.purchase_remove, name='purchase_remove'),

    path('purse_app/income/', views.income, name='income'),
    path('purse_app/new_income/', views.new_income, name='new_income'),
    path('purse_app/income_edit/<int:pk>/', views.income_edit, name='income_edit'),
    path('purse_app/income_remove/<int:pk>/', views.income_remove, name='income_remove'),

    path('purse_app/credit/', views.credit, name='credit'),
    path('purse_app/credit_cards/', views.credit_cards, name='credit_cards'),
    path('purse_app/other_credits/', views.other_credits, name='other_credits'),

    path('purse_app/debit/', views.debit, name='debit'),
    path('purse_app/debit_cards/', views.debit_cards, name='debit_cards'),
    path('purse_app/other_debits/', views.other_debits, name='other_debits'),

    path('accounts/new_user/', views.new_user, name='new_user'),
]
