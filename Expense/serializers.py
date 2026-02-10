# from rest_framework import serializers
# from .models import Expanse

# class ExpanseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model:Expanse
#         fiels='__all__'
from rest_framework import serializers
from .models import Expanse   # make sure this model exists

class ExpanseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanse
        fields = '__all__'