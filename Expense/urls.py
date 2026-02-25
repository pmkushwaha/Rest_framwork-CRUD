from django.urls import path
from .views import ExpenseApi , ExpenseUpApi,LoginView
 
 


urlpatterns = [
    path('expense',ExpenseApi.as_view(), name='ExpenseApi'),
 path('expense/<int:id>/',ExpenseUpApi.as_view(),name='ExpenseUpApi'),
 path('login',LoginView.as_view(),name='LoginView'),
            ]