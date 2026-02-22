from rest_framework import serializers
from products.models import ProductModel

class ProductListSerializers(serializers.ModelSerializer):
    stock_status = serializers.SerializerMethodField(read_only = True)

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
            "deleted_at",
            "created_at",
            "updated_at",
            "stock_quantity",
        ]
        read_only_fields = ["id", "created_by", "updated_at, deleted_at"]

        # Field Validation

        def validate_cost_price(self, value):
            if value < 0:
                raise serializers.ValidationError("Cost price cannot be negative")
            return value

        def validated_selling_price(self, value):
            if value < 0:
                raise serializers.ValidationError("Selling price cannot be negative.")
            return value


        # Object validation

        def validate(self, data):

            cost = data.get("cost_price")
            selling = data.get("selling_price")

            if cost is not None and selling is not None:
                if selling < cost:
                    raise serializers.ValidationError(
                        "Selling price cannot be lover than cost price."
                    ) 
                
            
            if self.instance and "sku" in data:
                raise serializers.ValidationError(
                    {"sku" : "SKU cannot be changed once created."}
                )
            return data