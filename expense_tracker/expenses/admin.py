from django.contrib import admin
from .models import Expense, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'is_default']
    list_filter = ['is_default']
    search_fields = ['name']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'date', 'category', 'note']
    list_filter = ['date', 'category']
    search_fields = ['user__username', 'note']
    date_hierarchy = 'date'