from django.db import models
from django.conf import settings
from django.utils import timezone


class Summary(models.Model):
    cash = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_debit = models.DecimalField(max_digits=10, decimal_places=2)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    budget_line = models.ForeignKey('PurchaseBudgetLine', to_field='line', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100)
    with_credit_card = models.ForeignKey(
        'CreditCards', to_field='name', null=True, blank=True, on_delete=models.SET_NULL
    )
    with_debit_card = models.ForeignKey('DebitCards', to_field='name', null=True, blank=True, on_delete=models.SET_NULL)

    def submit(self):
        if not self.date:
            self.date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.date} {self.amount} {self.budget_line} {self.comment}'


class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    budget_line = models.ForeignKey('IncomeBudgetLine', to_field='line', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100)
    to_debit_card = models.ForeignKey('DebitCards', to_field='name', null=True, blank=True, on_delete=models.SET_NULL)

    def submit(self):
        if not self.date:
            self.date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.date} {self.amount} {self.budget_line} {self.comment}'


class PurchaseBudgetLine(models.Model):
    line = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f'{self.line}'


class IncomeBudgetLine(models.Model):
    line = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f'{self.line}'


class DebitCards(models.Model):
    name = models.CharField(max_length=40, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'


class OtherDebits(models.Model):
    name = models.CharField(max_length=40, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.amount}'


class CreditCards(models.Model):
    name = models.CharField(max_length=40, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    grace_period_end = models.DateField(default=timezone.localdate)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class OtherCredits(models.Model):
    name = models.CharField(max_length=40, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.amount}'