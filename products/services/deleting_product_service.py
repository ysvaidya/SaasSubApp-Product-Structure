from django.utils import timezone

class RemovelProductService:
    @staticmethod
    def soft_delete_product(self, product):
        
        if product.is_deleted:
            raise ValueError(
                "Product is already deleted."
            )
        
        if product.stock_quantity > 0:
            raise ValueError("Cannot delete product with remaining stock.")
            
        product.is_deleted = True
        product.is_active = False
        product.deleted_at = timezone.now()
        product.save()

        return product