from rest_framework import serializers
from products.models import ProductModel

class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "product_name",
            "created_by",
            "sku",
            "cost_price",
            "stock_quantity",
            "selling_price",
            "supplier_name",
            "category",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_by",
            "cost_price",
            "stock_quantity",
            "sku",
            "created_at",
            "updated_at",
            "is_active",
        ]

    def validate_product_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Product Name cannot be Empty."
            )
        return value
    
    def validate_supplier_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Supplier Name cannot be Empty."
            )
        return value
    
    def validate_cost_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Cost price cannot be negative")
        return value

    def validate_selling_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Selling price cannot be negative")
        return value
    
    def validate(self, data):
        
        """
        Ensure selling_price is not lower than cost_price.
        Must handle PATCH correctly.
        """

    # Use new value if provided, otherwise fallback to existing value
        cost = data.get("cost_price", self.instance.cost_price)
    # Same goes to selling.
        selling = data.get("selling_price", self.instance.selling_price)

        if cost is not None and selling is not None:
            if selling < cost:
                raise serializers.ValidationError(
                    "Selling price cannot be lover than cost price."
                ) 
            
        return data