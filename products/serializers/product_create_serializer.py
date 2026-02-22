from rest_framework import serializers
from products.models import ProductModel

class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductModel
        fields = [
            "id",
            "product_name",
            "created_by",
            "sku",
            "cost_price",
            "selling_price",
            "supplier_name",
            "category",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id",
                            "created_by",
                            "created_at",
                            "updated_at",
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

        cost = data.get("cost_price")
        selling = data.get("selling_price")

        if cost is not None and selling is not None:
            if selling < cost:
                raise serializers.ValidationError(
                    "Selling price cannot be lower than cost price."
                ) 
            
        return data