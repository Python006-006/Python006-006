from django.shortcuts import render

# Create your views here.


from .models import Orders
from .serializers import OrdersSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from firstorder.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from firstorder.serializers import UserSerializer
from rest_framework.decorators import api_view

class OrderAPIViewSet(viewsets.ModelViewSet):
    """
    使用serializers和viewset
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'orders': reverse('orders-list', request=request, format=format)
    })

