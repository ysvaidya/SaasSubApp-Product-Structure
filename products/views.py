from django.shortcuts import render

# Apis import files 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from django.core.exceptions import ValidationError
import logging
logger = logging.getLogger(__name__)

from products.serializers.product_create_serializer import ProductCreateSerializer
from products.serializers.product_details_serializer import ProductDetailSerializer, ProductListSerializer, ProductPrivateSerializer
from products.serializers.product_update_serializer import ProductUpdateSerializer

from products.services.create_product_service import ProductServices
from products.services.update_product_service import ProductUpdateService
from products.services.deleting_product_service import RemovelProductService

from .models import ProductModel, InventoryMovement

# Create your views here.
def index (request):
    return render(request, "index.html")

# Post Creation
class ProductCreateView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):

        serializer = ProductCreateSerializer(
            data = request.data,
            context = {"request": request}
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = serializer.validated_data

        try:
            product = ProductServices.create_product(data, request.user)

        except ValidationError as e:
            return Response({"error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
        except PermissionError as e:
            return Response({"error" : 'Not allowed.'}, status = status.HTTP_403_FORBIDDEN)
        
        return Response (product.data, status = status.HTTP_201_CREATED) 



# List and Details of the Product
class ProductListView(APIView):
    
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        queryset = ProductModel.objects.filter(is_active = True).order_by("-created_at")
        serializer = ProductListSerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductDetailView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, pk):
        try:
            product = ProductModel.objects.filter(pk = pk, is_active = True)

        except ProductModel.DoesNotExist:
            return Response(
                {"error": "Product not Found."},
                status = status.HTTP_404_NOT_FOUND
            )


        serializer = ProductDetailSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductInventoryMovement(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, pk):
        try:
            productInv_move = InventoryMovement.object.filter(pk = pk, is_active = True)
        except InventoryMovement.DoesNotExist:
            return Response(
                {"error": "Product not Found"},
                status = status.HTTP_404_NOT_FOUND
            )
        
        serializer = ProductPrivateSerializer(productInv_move, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class ProductUpdateView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def patch(self, request, pk):

        try:
            product = ProductModel.objects.get(pk=pk, is_active=True)
        except ProductModel.DoesNotExist:
            return Response(
                {"error": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductUpdateSerializer(
            product,
            data  = request.data,
            partial = True,
            contex = {"request": request}
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = serializer.validated_data

        try:
            updated_product = ProductUpdateService.update_product(product, data, request.user)
        except ValidationError as e:
            return Response({"error": str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
        response_serializer = ProductDetailSerializer(updated_product)
        
        return Response (response_serializer, status = status.HTTP_202_ACCEPTED)
    


class ProductSoftDeleteView(APIView):
    
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def delete(self, request, pk):
        try:
            product = ProductModel.objects.filter(pk = pk, is_active = True)
        except ProductModel.DoesNotExist:
            return Response(
                {"error":"Product not Found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        try:
            RemovelProductService.soft_delete_product(
                product,
                request.user,
            )
        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except PermissionError:
            return Response(
                {"error": "Not allowed."},
                status=status.HTTP_403_FORBIDDEN
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
