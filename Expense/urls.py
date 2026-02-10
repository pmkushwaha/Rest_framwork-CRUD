from django.urls import path
from .views import ExpenseApi


urlpatterns = [
    path('expense',ExpenseApi.as_view(), name='ExpenseApi'),
 
]