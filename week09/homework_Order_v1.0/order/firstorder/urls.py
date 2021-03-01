
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from firstorder import views
from django.conf.urls import include

router = DefaultRouter()
router.register(r'orders', views.OrderAPIViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
