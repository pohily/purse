from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


from .models import *
from .forms import *


@login_required
def purse_app_start(request):
    ''' Стартовая страница'''
    try:
        summ = Summary.objects.get(owner=request.user)
        return render(
            request,
            'purse_app/start.html',
            {'cash': summ.cash, 'total': summ.total, 'total_debit': summ.total_debit, 'total_credit': summ.total_credit}
        )
    except Summary.DoesNotExist:
        return redirect('summary_settings')



@login_required
def statistics(request):
    ''' Вывод статистики и аналитики '''
    return render(request, 'purse_app/statistics.html')


@login_required
def settings(request):
    ''' Вывод существующих статей расхода/дохода'''
    pline = PurchaseBudgetLine.objects.filter(owner=request.user)
    iline = IncomeBudgetLine.objects.filter(owner=request.user)
    return render(request, 'purse_app/settings.html', {'pline': pline, 'iline': iline})


@login_required
def summary_settings(request):
    header = 'Первоначальные финансовые данные'
    extra = 'Внесите данные о всех ваших финансовых средствах для корректного ведения статистики в Purse'
    if request.method == "POST":
        form = SummaryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.total = item.cash + item.total_debit - item.total_credit
            item.save()
            return redirect('settings')
    else:
        try:
            summ = Summary.objects.get(owner=request.user)
            return redirect('summary_settings_edit', pk=summ.pk)
        except Summary.DoesNotExist:
            form = SummaryForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header, 'extra': extra})


@login_required
def summary_settings_edit(request, pk):
    header = 'Внимание! Редактирование первоначальных финансовых данных следует выполнять в крайне аккуратно.'
    item = get_object_or_404(Summary, pk=pk)
    if request.method == "POST":
        form = SummaryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = SummaryForm(instance=item)
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def purchase_bl(request):
    header = 'Новая статья расходов'
    if request.method == "POST":
        form = PurchaseBlForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('settings')
    else:
        form = PurchaseBlForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def income_bl(request):
    header = 'Новая статья доходов'
    if request.method == "POST":
        form = IncomeBlForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('settings')
    else:
        form = IncomeBlForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def income(request):
    ''' Вывод последних приходных накладных'''
    incomes = Income.objects.filter(owner=request.user).order_by('date')[:10]
    return render(request, 'purse_app/income.html', {'incomes': incomes})


@login_required
def new_income(request):
    header = 'Новая накладная'

    if request.method == "POST":
        form = IncomeForm(request.user, request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            summ = Summary.objects.get(owner=item.owner)
            try:
                if item.debit_name:
                    deb_car = DebitCards.objects.filter(owner=item.owner).get(debit_name=item.debit_name)
                    deb_car.amount += item.amount
                    deb_car.save()
                    summ.total_debit += item.amount
                else:
                    summ.cash += item.amount
            except AttributeError:
                pass
            summ.total += item.amount
            summ.save()
            item.save()
            return redirect('income')
    else:
        form = IncomeForm(request.user)
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def income_edit(request, pk):
    header = 'Редактирование накладной'
    item = get_object_or_404(Income, pk=pk)
    if request.method == "POST":
        form = IncomeForm(request.user, request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('income')
    else:
        form = IncomeForm(request.user, instance=item)
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def income_remove(request, pk):
    item = get_object_or_404(Income, pk=pk)
    item.delete()
    return redirect('income')


@login_required
def purchase(request):
    ''' Вывод последних расходных накладных'''
    purchases = Purchase.objects.filter(owner=request.user).order_by('date')[:10]
    return render(request, 'purse_app/purchase.html', {'purchases': purchases})


@login_required
def new_purchase(request):
    header = 'Новая накладная'
    if request.method == "POST":
        form = PurchaseForm(request.user, request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            summ = Summary.objects.get(owner=item.owner)
            try:
                if item.credit_name:
                    cr_car = CreditCards.objects.filter(owner=item.owner).get(credit_name=item.credit_name)
                    cr_car.amount += item.amount
                    cr_car.credit_limit -= item.amount
                    cr_car.save()
                    summ.total_credit += item.amount
                elif item.debit_name:
                    deb_car = DebitCards.objects.filter(owner=item.owner).get(debit_name=item.debit_name)
                    deb_car.amount -= item.amount
                    deb_car.save()
                    summ.total_debit -= item.amount
                else:
                    summ.cash -= item.amount
            except AttributeError:
                pass
            summ.total -= item.amount
            summ.save()
            item.save()
            return redirect('purchase')
    else:
        form = PurchaseForm(request.user)
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def purchase_edit(request, pk):
    header = 'Редактирование накладной'
    item = get_object_or_404(Purchase, pk=pk)
    if request.method == "POST":
        form = PurchaseForm(request.user, request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('purchase')
    else:
        form = PurchaseForm(request.user, instance=item)
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def purchase_remove(request, pk):
    item = get_object_or_404(Purchase, pk=pk)
    item.delete()
    return redirect('purchase')


@login_required
def debit(request):
    ''' Вывод существующих депозитов'''
    deb = chain(OtherDebits.objects.filter(owner=request.user), DebitCards.objects.filter(owner=request.user))
    return render(request, 'purse_app/debit.html', {'deb': deb})


@login_required
def debit_cards(request):
    header = 'Новая дебетовая карта'
    if request.method == "POST":
        form = DebitCardsForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('debit')
    else:
        form = DebitCardsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def other_debits(request):
    header = 'Новый депозит/долг'
    if request.method == "POST":
        form = OtherDebitsForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('debit')
    else:
        form = OtherDebitsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def credit(request):
    ''' Вывод существующих кредитов и кредиток '''
    otherCredits = OtherCredits.objects.filter(owner=request.user)
    creditCards = CreditCards.objects.filter(owner=request.user)
    return render(request, 'purse_app/credit.html', {'otherCredits': otherCredits, 'creditCards': creditCards})


@login_required
def credit_cards(request):
    header = 'Новая кредитная карта'
    if request.method == "POST":
        form = CreditCardsForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('credit')
    else:
        form = CreditCardsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def other_credits(request):
    header = 'Новый кредит'
    if request.method == "POST":
        form = OtherCreditsForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('credit')
    else:
        form = OtherCreditsForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})


@login_required
def stats(request):
    ''' Статистика и фильтры'''
    return render(request, 'purse_app/stats.html', {})


def new_user(request):
    header = 'Новый пользователь'
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('purse_app_start')
    else:
        form = UserCreationForm()
    return render(request, 'purse_app/edit_form.html', {'form': form, 'header': header})