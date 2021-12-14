from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):    # for /api/products route
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):    # for /api/products route
        pass

    def retrieve(self, request, pk=None):   # for /api/products/<id:str>
        pass

    def update(self, request, pk=None):   # for /api/products/<id:str>
        pass

    def destroy(self, request, pk=None):   # for /api/products/<id:str>
        pass
