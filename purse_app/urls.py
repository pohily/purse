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

    path('purse_app/income/', views.income, name='income'),
    path('purse_app/new_income/', views.new_income, name='new_income'),
    path('purse_app/income_edit/<int:pk>/', views.income_edit, name='income_edit'),
]
