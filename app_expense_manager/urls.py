from django.urls import path
from .views import index, add_expense
urlpatterns = [
    path('', index, name='index'),
    path('add_expense', add_expense, name='add_expense')
]