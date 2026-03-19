
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework  import  status
from rest_framework.permissions import IsAuthenticated ,AllowAny
from django.contrib.auth.models import User
from .permissions import isWoner
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Expanse
from .serializers import ExpanseSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
# test view for frontend
class TestView(APIView):
    permission_classes=[AllowAny]
    def get (self, request):
        return Response ({"message": " Hello from the DRF backend "})
    
class ExpenseApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        
        data = Expanse.objects.filter(user=request.user)
        serializer=ExpanseSerializer(data,many=True) 
        return Response(serializer.data )
   

    def post(self ,request):
        serializer=ExpanseSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return  Response( {"Message ": "Data saved successfully"})
        else:
            return Response(serializer.errors )
class ExpenseUpApi(APIView):
    permission_classes=[IsAuthenticated ,isWoner]
    def get(self,request,id):
                    
            data=Expanse.objects.get(id=id,user=request.user)
            if data is not None:
                serializer=ExpanseSerializer(data)
                return Response(serializer.data)
            else:
                return Response(serializer.errors) 
    def patch(self ,request, id ):
        item=Expanse.objects.get(id=id)
        serialiser=ExpanseSerializer(item,data=request.data, partial = True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({"Message":"Message Updated successfully"})
        else:
            return Response(serialiser.errors)
    def put(self,request,id):
        item=Expanse.objects.get(id=id)
        serializer=ExpanseSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.error_messages)
        
    def delete(self ,request,id):
        item=Expanse.objects.get(id=id)
        if  item:
            item.delete()
            return Response( status=status.HTTP_200_OK)
        else:
            return Response( status=status.HTTP_404_NOT_FOUND)
        

class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })

        return Response({"error": "Invalid credentials"}, status=400)


# LogOut View
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_Token=request.data.get('refresh')
            if refresh_Token is None:
                return Response("please provide the refresh Token")
            token=RefreshToken(refresh_Token)
            token.blacklist()
            return Response( "Logout Successfully ")
        except  Exception:
            return Response("Invalid refresh Token")
