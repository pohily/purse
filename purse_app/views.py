from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from .forms import *


@login_required
def purse_app_start(request):
    return render(request, 'purse_app/start.html', {})


@login_required
def settings(request):
    pline = PurchaseBudgetLine.objects.all()
    iline = IncomeBudgetLine.objects.all()
    return render(request, 'purse_app/settings.html', {'pline': pline, 'iline': iline})


@login_required
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


@login_required
def purchase_bl(request):
    if request.method == "POST":
        form = PurchaseBlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = PurchaseBlForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


@login_required
def income_bl(request):
    if request.method == "POST":
        form = IncomeBlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = IncomeBlForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


@login_required
def income(request):
    incomes = Income.objects.all().order_by('date')[:10]
    return render(request, 'purse_app/income.html', {'incomes': incomes})


@login_required
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


@login_required
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


@login_required
def purchase(request):
    purchases = Purchase.objects.all().order_by('date')[:10]
    return render(request, 'purse_app/purchase.html', {'purchases': purchases})


@login_required
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


@login_required
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


@login_required
def debit(request):
    deb = chain(OtherDebits.objects.all(), DebitCards.objects.all())
    return render(request, 'purse_app/debit.html', {'deb': deb})


@login_required
def debit_cards(request):
    if request.method == "POST":
        form = DebitCardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('debit')
    else:
        form = DebitCardsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


@login_required
def other_debits(request):
    if request.method == "POST":
        form = OtherDebitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('debit')
    else:
        form = OtherDebitsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


@login_required
def credit(request):
    otherCredits = OtherCredits.objects.all()
    creditCards = CreditCards.objects.all()
    return render(request, 'purse_app/credit.html', {'otherCredits': otherCredits, 'creditCards': creditCards})


@login_required
def credit_cards(request):
    if request.method == "POST":
        form = CreditCardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credit')
    else:
        form = CreditCardsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


@login_required
def other_credits(request):
    if request.method == "POST":
        form = OtherCreditsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credit')
    else:
        form = OtherCreditsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})


@login_required
def stats(request):
    return render(request, 'purse_app/stats.html', {})


def new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            User.objects.create_user(form.cleaned_data["fullname", "password"])
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'purse_app/edit_form.html', {'form': form})