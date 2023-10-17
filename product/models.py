from django.db import models

# Create your models here.

class ProductStatus(models.TextChoices):
    """
    gender choices between Male, Female, Not Specified
    """

    UPDATED = ("updated", "Updated")
    ACTIVE = ("active", "Active")



class Product(models.Model):
    part_number = models.CharField(max_length=120,unique=True)
    part_number_new = models.CharField(max_length=120,null=True,blank=True)
    part_number_description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="product_image/")
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=50)

    @property
    def price(self):
        return self.prices.all().first().price
    
class ProductPrices(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="prices")
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=100,null=True,blank=True)
    name = models.CharField(max_length=120,null=True,blank=True)


class SearchHistory(models.Model):
    query = models.CharField(max_length=300)
    