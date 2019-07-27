from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *


def purse_app_start(request):
    return render(request, 'purse_app/start.html', {})


def settings(request):
    pline = PurchaseBudgetLine.objects.all()
    iline = IncomeBudgetLine.objects.all()
    return render(request, 'purse_app/settings.html', {'pline': pline, 'iline': iline})


def summary_settings(request):
    if request.method == "POST":
        form = SummaryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.total = item.cash + item.total_debit - item.total_credit
            item.save()
            return redirect('settings')
    else:
        form = SummaryForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def purchase_bl(request):
    if request.method == "POST":
        form = PurchaseBlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = PurchaseBlForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def income_bl(request):
    if request.method == "POST":
        form = IncomeBlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = IncomeBlForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def income(request):
    incomes = Income.objects.all().order_by('date')[:10]
    return render(request, 'purse_app/income.html', {'incomes': incomes})


def new_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('income')
    else:
        form = IncomeForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def income_edit(request, pk):
    item = get_object_or_404(Income, pk=pk)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('income')
    else:
        form = IncomeForm(instance=item)
    return render(request, 'purse_app/edit_form.html', {'form': form})


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
    return render(request, 'purse_app/edit_form.html', {'form': form})


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
    return render(request, 'purse_app/edit_form.html', {'form': form})


def debit(request):
    deb = chain(OtherDebits.objects.all(), DebitCards.objects.all())
    return render(request, 'purse_app/debit.html', {'deb': deb})


def debit_cards(request):
    if request.method == "POST":
        form = DebitCardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('debit')
    else:
        form = DebitCardsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def other_debits(request):
    if request.method == "POST":
        form = OtherDebitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('debit')
    else:
        form = OtherDebitsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def credit(request):
    otherCredits = OtherCredits.objects.all()
    creditCards = CreditCards.objects.all()
    return render(request, 'purse_app/credit.html', {'otherCredits': otherCredits, 'creditCards': creditCards})


def credit_cards(request):
    if request.method == "POST":
        form = CreditCardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credit')
    else:
        form = CreditCardsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def other_credits(request):
    if request.method == "POST":
        form = OtherCreditsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credit')
    else:
        form = OtherCreditsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


def stats(request):
    return render(request, 'purse_app/stats.html', {})