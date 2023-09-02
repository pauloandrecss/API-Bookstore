from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()