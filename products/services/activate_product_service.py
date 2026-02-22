class ActivationProductService:

    def activate_product(self, product):

        if product.is_active:
            raise ValueError(
                "Product is already Activated. No changes will happen."
            )
        
        product.is_activa = True
        product.save()