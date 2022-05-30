import django_filters.rest_framework
from django.db.models import Q
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Customer, Type
from .serializers import CustomerSerializer, TypeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']

    @action(methods=['GET'], detail=False)
    def rentype(self, request):
        types = Type.objects.all()
        return Response({'types': [type.name for type in types]})

    @action(methods=['POST'], detail=False)
    def addrentype(self, request, pk=None):
        rentype = self.queryset.create(name=request.data.get('name'))
        rentype.save()
        return Response({'new_type': "success"})


class GetCustomerFromCustomerView(ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Customer.objects.filter(name=name)


class GetRomaCustomerView(ListAPIView):
    queryset = Customer.objects.filter(Q(name='roma') | Q(name='Roma'))
    serializer_class = CustomerSerializer










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
