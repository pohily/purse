from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ('date', 'budget_line', 'amount', 'comment',)
        labels = {
            'date': _('Дата'),
            'budget_line': _('Статья'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
        }


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ('date', 'budget_line', 'amount', 'comment',)
        labels = {
            'date': _('Дата'),
            'budget_line': _('Статья'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
        }


class SummaryForm(forms.ModelForm):

    class Meta:
        model = Summary
        fields = ('cash', 'total_debit', 'total_credit', )
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