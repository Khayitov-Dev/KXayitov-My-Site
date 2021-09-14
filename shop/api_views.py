from django.db import models
from rest_framework.generics import ListCreateAPIView
from .serializers import ShopSerializer
from .models import Shop

class ShopListView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer