from django.shortcuts import render

def index(request):
    return render(request, 'app_expense_manager/index.html')

def add_expense(request):
    return render(request, 'app_expense_manager/add_expense.html')