
"""
    Issues
    1 cost price should not be updated
    2 sku can be but no.
    3 stock quantity.

"""

class ProductUpdateService:
    @staticmethod
    def update_product(self, data, product):

        if product.is_deleted:
            raise ValueError("You cannot Updated the product values.")


        if "selling_price" in data:
            selling = data.get("selling_price")
        else:
            selling = product.selling_price

        if "cost_price" in data:
            cost = data.get("cost_price")
        else:
            cost = product.cost_price

        if cost < 0:
            raise ValueError(
                "Cost Price can not be negative."
            )
        
        if selling < 0:
            raise ValueError(
                "Selling price can not be negative."
            )
        
        if selling < cost:
            raise ValueError(
                "Selling price cannot be lower than cost price."
            )
        
        margin = 0.10
        minimum_selling = cost / (1 - margin)

        if selling < minimum_selling :
            raise ValueError(
                f"Minimum selling price for 10% margin is {minimum_selling}. "
            )

        if "product_name" in data:
            product.product_name = data.get("product_name")

        if "supplier_name" in data:
            product.supplier_name = data.get("supplier_name")

        if "category" in data:
            product.category = data.get("category") 
            
        
        product.cost_price = cost
        product.selling_price = selling
        
        product.save()

        return product
    

# class movementInvUpdateService: