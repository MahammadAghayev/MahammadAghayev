from rest_framework import generics
from ..models import ProductItem
from .serializers import ProductItemSerializer
from rest_framework.response import Response


class ProductItemCreateAPIView(generics.CreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.user = request.user
        instance.save()

        data = serializer.data



        return Response({"detail": "OK", 'data': data}, status=201)