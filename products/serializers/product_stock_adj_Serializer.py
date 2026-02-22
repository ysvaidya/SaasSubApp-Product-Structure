from rest_framework import serializers
from products.models import ProductModel, InventoryMovement

class ProductStockAdjustmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InventoryMovement
        field = [
            'id',
            'product',
            'quantity',
            'movement_type',
            'reason',
            'created_by',
            'created_at',
        ]

        read_only_field = [
            'id',
            'created_by',
            'created_at',
        ]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be grater than zero."
            )
        return value
    
    def validate(self, data):
        product = data.get("product")
        quality = data.get("quantity")
        movement_type = data.get("movement_type")

        if movement_type =="OUT":
            if quality > ProductModel.stock_quantity:
                raise serializers.ValidationError(
                    "Insufficient stock avaiable."
                )
        return data
