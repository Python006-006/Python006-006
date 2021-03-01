from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Orders


class OrdersSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = ['url','id', 'orderid', 'order', 'createtime', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Orders.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'orders']