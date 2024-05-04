from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class ProductsAbout(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='products/',blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        db_table = 'products_about'

    def __str__(self):
        return f"{self.category.name} {self.model}"