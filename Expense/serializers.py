from rest_framework import serializers
from .models import Expanse    

class ExpanseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanse
        fields = '__all__'