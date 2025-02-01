from django.db import models
from django.core.validators import MinValueValidator
from Catalogue.models import Produit
# Create your models here.


class Panier(models.Model):
    produits = models.ManyToManyField(Produit)
    nombre_de_produits = models.IntegerField(
        validators=[MinValueValidator(0)]  # Nombre de produits ne peut pas être négatif
    )

    

class Vente(models.Model):
    date_vente = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit)
    quantite = models.IntegerField(
        validators=[MinValueValidator(0)]  # Quantité ne peut pas être négative
    )
    montant_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]  # Montant total ne peut pas être négatif
    )


class MobileMoney(models.Model):
    TYPE_PAIEMENT_CHOICES = [
        ('yas', 'Yas'),
        ('flooz', 'Flooz'),
    ]

    date_payement = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]  # Montant ne peut pas être négatif
    )
    type_paiement = models.CharField(max_length=5, choices=TYPE_PAIEMENT_CHOICES)
    
    
class Statistique(models.Model):
    def calculerVente(self):
        # Calcule le total des ventes (par exemple, somme des montants dans le modèle Vente)
        ventes = Vente.objects.all()
        total_ventes = sum(vente.montant_total for vente in ventes)
        return total_ventes