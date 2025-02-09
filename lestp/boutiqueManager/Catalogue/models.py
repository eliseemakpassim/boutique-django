from django.db import models
from django.core.validators import MinValueValidator

class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantite = models.IntegerField(validators=[MinValueValidator(0)])
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    
    # Ajout d'un champ temporaire pour la migration
    code_interne = models.CharField(max_length=10, blank=True, null=True)  # Ajout d'un champ temporaire

    def __str__(self):
        return f"{self.nom} ({self.categorie})"
