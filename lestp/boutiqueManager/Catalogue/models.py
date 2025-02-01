from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

   

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]  # Prix ne peut pas être négatif
    )
    quantite = models.IntegerField(
        validators=[MinValueValidator(0)]  # Quantité ne peut pas être négative
    )
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    
