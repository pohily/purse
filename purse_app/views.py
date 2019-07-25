from django.shortcuts import render

from .models import *


def purse_app_start(request):
    return render(request, 'purse_app/start.html', {})


def income(request):
    return render(request, 'purse_app/income.html', {})


def purchase(request):
    purchases = Purchase.objects.all().order_by('date')[:10]
    return render(request, 'purse_app/purchase.html', {'purchases': purchases})


def debit(request):
    return render(request, 'purse_app/debit.html', {})


def credit(request):
    return render(request, 'purse_app/credit.html', {})


def stats(request):
    return render(request, 'purse_app/stats.html', {})