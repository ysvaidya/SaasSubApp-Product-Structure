
class DeactivationProductService:

    def deactivate_product(self, product):

        if not product.is_active :
            raise ValueError("Inactive product cannot be sold")

        product.is_active = False
        product.save()

        return product