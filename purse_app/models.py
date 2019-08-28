from django.db import models
from django.conf import settings
from django.utils import timezone


class Summary(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    cash = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_debit = models.DecimalField(max_digits=10, decimal_places=2)
    total_credit = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    line = models.ForeignKey('PurchaseBudgetLine', blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100, blank=True)
    credit_name = models.ForeignKey('CreditCards', blank=True, null=True, on_delete=models.CASCADE)
    debit_name = models.ForeignKey('DebitCards', blank=True, null=True, on_delete=models.CASCADE)

    def submit(self):
        if not self.date:
            self.date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.date} {self.amount} {self.line} {self.comment}'


class Income(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    line = models.ForeignKey('IncomeBudgetLine', blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100, blank=True)
    debit_name = models.ForeignKey('DebitCards', blank=True, null=True, on_delete=models.CASCADE)

    def submit(self):
        if not self.date:
            self.date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.date} {self.amount} {self.line} {self.comment}'


class PurchaseBudgetLine(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    line = models.CharField(max_length=40)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'line'], name='unique_owner_pline')
        ]

    def __str__(self):
        return f'{self.line}'


class IncomeBudgetLine(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    line = models.CharField(max_length=40)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'line'], name='unique_owner_iline')
        ]

    def __str__(self):
        return f'{self.line}'


class DebitCards(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    debit_name = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'debit_name'], name='unique_owner_debit_card')
        ]

    def __str__(self):
        return f'{self.debit_name}'


class OtherDebits(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    debit_name = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'debit_name'], name='unique_owner_debit')
        ]

    def __str__(self):
        return f'{self.debit_name} {self.amount} {self.comment}'


class CreditCards(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    credit_name = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_limit = models.DecimalField(max_digits=10, default=1, decimal_places=2)
    grace_period_end = models.DateField(default=timezone.localdate)
    comment = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'credit_name'], name='unique_owner_credit_card')
        ]

    def __str__(self):
        return f'{self.credit_name}'


class OtherCredits(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    credit_name = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'credit_name'], name='unique_owner_credit')
        ]

    def __str__(self):
        return f'{self.credit_name} {self.amount} {self.comment}'