import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Customer, Type


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_email(self, attrs):
        email = attrs['email']
        if not email.find('@') and email.find('.'):
            raise serializers.ValidationError({'customer': "Некорректный адрес электронной почты"})
        return attrs



class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
