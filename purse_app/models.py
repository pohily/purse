from django.db import models
from django.conf import settings
from django.utils import timezone


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    budget_line = models.ForeignKey('PurchaseBudgetLine', to_field='line', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=200)

    def submit(self):
        if not self.date:
            self.date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.date} {self.amount} {self.budget_line_id} {self.comment[:20]} ...'


class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    budget_line = models.ForeignKey('IncomeBudgetLine', to_field='line', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=200)

    def submit(self):
        if not self.date:
            self.date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.date} {self.amount} {self.budget_line_id} {self.comment[:20]} ...'


class PurchaseBudgetLine(models.Model):
    line = models.CharField(max_length=40, unique=True)


class IncomeBudgetLine(models.Model):
    line = models.CharField(max_length=40, unique=True)
