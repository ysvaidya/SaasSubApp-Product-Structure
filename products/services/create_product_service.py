from django.db import transaction
from products.models import ProductModel, InventoryMovement
from django.utils import timezone

class ProductServices:

    @staticmethod
    def create_product(self, data, user):
        
        cost = data.get("cost_price")
        selling = data.get("selling_price")
        stock = data.get("stock_quantity", 0)
        

        if cost is None and cost < 0:
            raise ValueError(
                "Cost price must be a positive number"
            )
        
        if selling is None and selling < 0:
            raise ValueError(
                "Selling price must be a positive number"
            )
        
        if selling < cost:
            raise ValueError(
                "Selling price cannot be less than cost price"
            )
        
        margin = cost / (1- 0.10)
        
        if selling < margin:
            raise ValueError(
                f"Margin should be 10 percent at list. Selling price should be more that {cost}. "
            )
        
        if stock > 0 :

            with transaction.automic():

                product = ProductModel.objects.create(
                    product_name = data.get("product_name"),
                    sku = data.get("sku"), # Note: make a different function for it to give unique Id.
                    created_by = user,
                    cost_price = cost,
                    selling_price = selling,
                    supplier_name = data.get("supplier_name"),
                    stock_quantity = stock,
                    category = data.get("category"),
                    created_at = timezone.now(),
                    is_active = True
                ) 

                InventoryMovement.object.create(
                    product = product,
                    quentity = stock,
                    movement_type = "IN",
                    reason = "Opening Stock",
                    create_at = timezone.now()
                )

                return product
            
        else:

            product = ProductModel.objects.create(
                    product_name = data.get("product_name"),
                    sku = data.get("sku"), # Note: make a different function for it to give unique Id.
                    created_by = user,
                    cost_price = cost,
                    selling_price = selling,
                    supplier_name = data.get("supplier_name"),
                    stock_quantity = 0,
                    category = data.get("category"),
                    created_at = timezone.now(),
                    is_active = True
                ) 
            
            return product
        
