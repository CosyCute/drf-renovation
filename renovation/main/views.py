from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Type
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False)
    def rentype(self, request):
        types = Type.objects.all()
        return Response({'types': [type.name for type in types]})



# class CustomerAPIView(APIView):
#     def get(self, request):
#         lst = Customer.objects.all()
#         return Response({'customers': CustomerSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'customer': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Customer.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#         serializer = CustomerSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'customer': serializer.data})
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Customer.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object does not exist"})
#
#         return Response({'customer': "delete customer " + str(pk)})
