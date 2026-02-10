from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Expanse
from .serializers import ExpanseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class ExpenseApi(APIView):

    def get(self,request):
        data=Expanse.objects.all()
        serializer=ExpanseSerializer(data  ,many=True) 
        return Response(serializer.data )
   
    
    