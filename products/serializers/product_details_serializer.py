from rest_framework import serializers
from products.models import ProductModel, InventoryMovement

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields  = [
            "id",
            "product_name",
            "created_by",
            "selling_price",
            "category",
            "is_active",
        ]
        read_only_fields = [
            "product_name",
            "created_by",
            "selling_price",
            "category",
            "is_active"
        ]


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "product_name",
            "created_by",
            "cost_price",
            "sku",
            "selling_price",
            "supplier_name",
            "stock_quantity",
            "category",
            "is_active",
            "is_deleted",
            "created_at",
            "updated_at",
            "deleted_at",
        ]
        reade_only_fields = [
            "id",
            "sku",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

class ProductPrivateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryMovement
        fieilds = [
            "product",
            "quentity",
            "movement_type",
            "reason",
            "created_by",
        ]

