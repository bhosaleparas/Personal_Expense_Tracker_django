from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q  
from django.db import models  
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Expense, Category
from .forms import ExpenseForm, UserRegistrationForm
import json



def create_default_categories(user):
    default_categories = ['Food', 'Transport', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Other']
    for category_name in default_categories:
        Category.objects.get_or_create(
            name=category_name, 
            user=user,
            defaults={'is_default': False}
        )





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create default categories for the new user
            create_default_categories(user)
            
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})





@login_required
def dashboard(request):
    
    recent_expenses = Expense.objects.filter(user=request.user)[:5]
    
    
    
    # Monthly summary
    current_month = timezone.now().month
    current_year = timezone.now().year
    
    monthly_total = Expense.objects.filter(
        user=request.user,
        date__month=current_month,
        date__year=current_year
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    
    
    # Category-wise spending
    category_data = Expense.objects.filter(
        user=request.user,
        date__month=current_month,
        date__year=current_year
    ).values('category__name').annotate(total=Sum('amount')).order_by('-total')
    
    context = {
        'recent_expenses': recent_expenses,
        'monthly_total': monthly_total,
        'category_data': category_data,
    }
    return render(request, 'expenses/dashboard.html', context)




@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    
   
    category_filter = request.GET.get('category')
    month_filter = request.GET.get('month')
    
    if category_filter and category_filter != 'all':
        expenses = expenses.filter(category_id=category_filter)
    
    if month_filter:
        year, month = month_filter.split('-')
        expenses = expenses.filter(date__year=year, date__month=month)
    
   
    categories = Category.objects.filter(
        Q(user=request.user) | Q(is_default=True)
    )
    
    context = {
        'expenses': expenses,
        'categories': categories,
    }
    return render(request, 'expenses/expense_list.html', context)






@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.user, request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(user=request.user)
    
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Add Expense'})






@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        form = ExpenseForm(request.user, request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(user=request.user, instance=expense)
    
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Edit Expense'})





@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('expense_list')
    
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})



@login_required
def summary_report(request):
    
    year = request.GET.get('year', timezone.now().year)
    
    try:
        year = int(year)
    except (ValueError, TypeError):
        year = timezone.now().year
    
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    
    monthly_totals = []
    for month in range(1, 13):
        month_total = Expense.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month
        ).aggregate(total=Sum('amount'))['total'] or 0
        
        if month_total > 0:  
            monthly_totals.append({
                'month': month,
                'month_name': month_names[month],
                'total': month_total
            })
    
    
    # Category totals for the year
    category_totals = Expense.objects.filter(
        user=request.user,
        date__year=year
    ).values('category__name').annotate(
        total=Sum('amount')
    ).order_by('-total')
    
    
    
    # Yearly total
    yearly_total = Expense.objects.filter(
        user=request.user,
        date__year=year
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    
    
    #average monthly spend
    if monthly_totals:
        avg_monthly = sum(item['total'] for item in monthly_totals) / len(monthly_totals)
    else:
        avg_monthly = 0


    
    # Get available years  existing expenses 
    available_years = Expense.objects.filter(
        user=request.user
    ).dates('date', 'year')  
    

    year_values = sorted([date.year for date in available_years], reverse=True)

    
    # If no expenses yet, 
    if not year_values:
        year_values = [timezone.now().year]
    
    context = {
        'monthly_totals': monthly_totals,
        'category_totals': category_totals,
        'yearly_total': yearly_total,
        'avg_monthly': avg_monthly,
        'selected_year': year,
        'available_years': year_values,
    }
    return render(request, 'expenses/summary.html', context)