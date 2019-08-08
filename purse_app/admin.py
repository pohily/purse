from django.contrib import admin
from .models import Purchase, Income, PurchaseBudgetLine, IncomeBudgetLine, Summary

admin.site.register(Purchase)
admin.site.register(Income)
admin.site.register(PurchaseBudgetLine)
admin.site.register(IncomeBudgetLine)
admin.site.register(Summary)