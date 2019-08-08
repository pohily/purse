from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ('date', 'budget_line', 'amount', 'comment', 'with_credit_card', 'with_debit_card',)
        labels = {
            'date': _('Дата'),
            'budget_line': _('Статья'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
            'with_credit_card': _('Платеж кредиткой?'),
            'with_debit_card': _('Платеж дебетовкой?'),
        }


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ('date', 'budget_line', 'amount', 'comment', 'to_debit_card',)
        labels = {
            'date': _('Дата'),
            'budget_line': _('Статья'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
            'to_debit_card': _('На карту?'),
        }


class SummaryForm(forms.ModelForm):

    class Meta:
        model = Summary
        fields = ('cash', 'total_debit', 'total_credit',)
        labels = {
            'cash': _('Всего наличных'),
            'total_debit': _('Всего мне должны'),
            'total_credit': _('Всего я должен'),
        }


class PurchaseBlForm(forms.ModelForm):

    class Meta:
        model = PurchaseBudgetLine
        fields = ('line', )
        labels = {
            'line': _('Введите название новой расходной накладной'),
        }


class IncomeBlForm(forms.ModelForm):

    class Meta:
        model = IncomeBudgetLine
        fields = ('line', )
        labels = {
            'line': _('Введите название новой приходной накладной'),
        }


class CreditCardsForm(forms.ModelForm):

    class Meta:
        model = CreditCards
        fields = ('name', 'amount', 'credit_limit', 'grace_period_end', 'comment',)
        labels = {
            'name': _('Введите название новой кредитной карты'),
            'amount': _('Введите размер кредита'),
            'credit_limit': _('Введите размер кредитного лимита'),
            'grace_period_end': _('Введите дату окончания льготного периода'),
            'comment': _('Комментарий'),
        }


class OtherCreditsForm(forms.ModelForm):

    class Meta:
        model = OtherCredits
        fields = ('name', 'amount', 'comment',)
        labels = {
            'name': _('Введите название для этого кредита'),
            'amount': _('Введите размер кредита'),
            'comment': _('Комментарий'),
        }


class DebitCardsForm(forms.ModelForm):
    class Meta:
        model = DebitCards
        fields = ('name', 'amount', 'comment',)
        labels = {
            'name': _('Введите название новой дебетовой карты'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
        }


class OtherDebitsForm(forms.ModelForm):
    class Meta:
        model = OtherDebits
        fields = ('name', 'amount', 'comment',)
        labels = {
            'name': _('Введите название вашего депозита'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
        }