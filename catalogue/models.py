from django.db import models



class Category(models.Model):
    
    name = models.CharField(max_length=255, verbose_name="Nom de la catégorie")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    vendeur_id = models.IntegerField(verbose_name="ID du Vendeur", db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    
    
    name = models.CharField(max_length=255, verbose_name="Nom de l'article")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.IntegerField(default=0, verbose_name="Quantité en stock")
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
