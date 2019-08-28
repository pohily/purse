from django import forms
from django.utils.translation import gettext_lazy as _

from .models import *


class IncomeForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['line'].widget = forms.Select()
        self.fields['line'].queryset = IncomeBudgetLine.objects.filter(owner=user)
        self.fields['debit_name'].widget = forms.Select()
        self.fields['debit_name'].queryset = DebitCards.objects.filter(owner=user)


    class Meta:
        model = Income
        fields = ('date', 'line', 'amount', 'comment', 'debit_name',)
        labels = {
            'date': _('Дата'),
            'line': _('Статья'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
            'debit_name': _('На карту?'),
        }


class PurchaseForm(IncomeForm):

    def __init__(self, user, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['line'].widget = forms.Select()
        self.fields['line'].queryset = PurchaseBudgetLine.objects.filter(owner=user)
        self.fields['debit_name'].widget = forms.Select()
        self.fields['debit_name'].queryset = DebitCards.objects.filter(owner=user)
        self.fields['credit_name'].widget = forms.Select()
        self.fields['credit_name'].queryset = CreditCards.objects.filter(owner=user)

    class Meta:
        model = Purchase
        fields = ('date', 'line', 'amount', 'comment', 'credit_name', 'debit_name',)
        labels = {
            'credit_name': _('Платеж кредиткой?'),
            'debit_name': _('Платеж дебетовкой?'),
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
        fields = ('credit_name', 'amount', 'credit_limit', 'grace_period_end', 'comment',)
        labels = {
            'credit_name': _('Введите название новой кредитной карты'),
            'amount': _('Введите размер кредита'),
            'credit_limit': _('Введите размер кредитного лимита'),
            'grace_period_end': _('Введите дату окончания льготного периода'),
            'comment': _('Комментарий'),
        }


class OtherCreditsForm(forms.ModelForm):

    class Meta:
        model = OtherCredits
        fields = ('credit_name', 'amount', 'comment',)
        labels = {
            'credit_name': _('Введите название для этого кредита'),
            'amount': _('Введите размер кредита'),
            'comment': _('Комментарий'),
        }


class DebitCardsForm(forms.ModelForm):
    class Meta:
        model = DebitCards
        fields = ('debit_name', 'amount', 'comment',)
        labels = {
            'debit_name': _('Введите название новой дебетовой карты'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
        }


class OtherDebitsForm(forms.ModelForm):
    class Meta:
        model = OtherDebits
        fields = ('debit_name', 'amount', 'comment',)
        labels = {
            'debit_name': _('Введите название вашего депозита'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
        }