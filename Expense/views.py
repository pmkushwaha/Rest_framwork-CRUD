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
        serializer=ExpanseSerializer(data,many=True) 
        return Response(serializer.data )
   

    def post(self ,request):
        serializer=ExpanseSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return  Response( {"Message ": "Data saved successfully"})
    

class ExpenseUpApi(APIView):

    def get(self,request,id):
        data=Expanse.objects.get(id=id)
        serializer=ExpanseSerializer(data)
        return Response(serializer.data)
             
    def patch(self ,request, id ):
        item=Expanse.objects.get(id=id)
        serialiser=ExpanseSerializer(item,data=request.data, partial = True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({"Message":"Message Updated successfully"})
        else:
            return Response(serialiser.errors)

