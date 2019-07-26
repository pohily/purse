from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Purchase, Income


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