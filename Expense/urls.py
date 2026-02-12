from django.urls import path
from .views import ExpenseApi , ExpenseUpApi
 
 


urlpatterns = [
    path('expense',ExpenseApi.as_view(), name='ExpenseApi'),
 path('expense/<int:id>/',ExpenseUpApi.as_view(),name='ExpenseUpApi'),
 
]