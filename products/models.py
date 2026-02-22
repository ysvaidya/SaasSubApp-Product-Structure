from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class ProductModel(models.Model):

    
    class Categories(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name

    product_name = models.CharField( 
        max_length=20,
        blank=False,
        null=False,
    )

    created_by = models.ForeignKey( 
        User,
        on_delete=models.SET_NULL,
        related_name="User_created_products",
        null = True,
    )

    sku = models.CharField( 
        max_length=50,
        unique=True,
        db_index=True, # Faster search when selling product by SKU
    )

    cost_price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        null = False,
        blank = False,
        validators = [MinValueValidator(0)], # more than Zero
        help_text= "Actual Price of the product."
    )

    selling_price = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        null = False,
        blank = False,
        validators = [MinValueValidator(0)], # more than Zero
        help_text= "Selling Price of the product."
    )

    supplier_name = models.CharField( 
        max_length=50,
        blank = False,
        null = False,
    )

    stock_quantity = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(
         'Categories',
        on_delete=models.PROTECT,
        related_name="products_type",
    )

    is_active = models.BooleanField( default = True)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=False)

    updated_at = models.DateTimeField( auto_now=False)

    deleted_at = models.DateTimeField(null = True, blank = True)

    def clean(self):
        if self.selling_price < self.cost_price:
            raise ValidationError(
                {
                    "selling_price": "Selling price must be greater than or equal to actual price."
                }
            )
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save(update_fields=["is_active", " deleted_at "])


class InventoryMovement(models.Model):
    CHOICES =(
        ('IN','Stock In'),
        ('OUT','Stock out'),
        ('ADJ','Adjustment'),

    )

    product = models.ForeignKey(
        ProductModel, 
        on_delete=models.PROTECT,
        related_name = "stock_movements"
    )
    quentity = models.PositiveIntegerField(
        default = 0,
        help_text = "Available stock quantity"
    )
    
    movement_type = models.CharField(
        max_length=50,
        choices = CHOICES,
    )

    reason = models.TextField(
        ("Reason"), 
        blank = True,
        help_text="Optional explanation for stock change."
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null = True,
        related_name = "invoentory_movements",
    )
    created_at = models.DateTimeField(auto_now_add=True)


