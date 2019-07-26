from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import PurchaseForm


def purse_app_start(request):
    return render(request, 'purse_app/start.html', {})


def income(request):
    return render(request, 'purse_app/income.html', {})


def purchase(request):
    purchases = Purchase.objects.all().order_by('date')[:10]
    return render(request, 'purse_app/purchase.html', {'purchases': purchases})


def new_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('purchase')
    else:
        form = PurchaseForm()
    return render(request, 'purse_app/purchase_edit.html', {'form': form})


def purchase_edit(request, pk):
    item = get_object_or_404(Purchase, pk=pk)
    if request.method == "POST":
        form = PurchaseForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('purchase')
    else:
        form = PurchaseForm(instance=item)
    return render(request, 'purse_app/purchase_edit.html', {'form': form})


def debit(request):
    return render(request, 'purse_app/debit.html', {})


def credit(request):
    return render(request, 'purse_app/credit.html', {})


def stats(request):
    return render(request, 'purse_app/stats.html', {})