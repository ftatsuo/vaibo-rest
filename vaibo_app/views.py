from .models import Smartphone
from .serializer import SmartphoneSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class SmartphoneViewSet(viewsets.ModelViewSet):
  queryset = Smartphone.objects.all()
  serializer_class = SmartphoneSerializer
  
  # DjangoFilterBackend procura por campo, somente busca exata, por exemplo, 
  # se procurar por "XPeria" no campo 'product' não acha "XPeria 5" ou "Xperia Pro"
  # filter_backends = [DjangoFilterBackend]
  # filterset_fields = ['product', 'brand', 'vaibo_score']
  
  # filters.SearchFilter procura nos campos especificados no search_fields
  # retorna os valores encontrados mesmo com termos parciais de procura, por exemplo, 
  # se procurar "XPeria" retorna "Xperia 5" e "Xperia Pro", se procurar por "phone",
  # retorna "iPhone 13"
  filter_backends = [filters.SearchFilter]
  search_fields = ['product', 'brand']

  # filters.OrderingFilter ordena de acordo com o campo do ordering_fields
  # filter_backends = [filters.OrderingFilter]
  # ordering_fields = ['product']

  # filter configuration
  # '^' starts with search
  # ex: search_fields = ['^product', '^brand']
  # '=' exact search
  # ex: search_fields = ['=product', '=brand']
  # '@' full text search (only postgre)
  # '$' regex search