from django.db import models
from django.core.validators import MinValueValidator
from Catalogue.models import Produit

class Panier(models.Model):
    produits = models.ManyToManyField(Produit)
    nombre_de_produits = models.IntegerField(
        validators=[MinValueValidator(0)]  # Nombre de produits ne peut pas être négatif
    )
    # Ajout d'un champ temporaire pour permettre la migration
    code_interne = models.CharField(max_length=10, blank=True, null=True)  # Champ temporaire

    def __str__(self):
        return f"Panier contenant {self.nombre_de_produits} produit(s)"

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
    # Ajout d'un champ temporaire pour permettre la migration
    code_interne = models.CharField(max_length=10, blank=True, null=True)  # Champ temporaire

    def __str__(self):
        return f"Vente du {self.date_vente.strftime('%d-%m-%Y')} avec {self.quantite} produit(s) pour un total de {self.montant_total} FCFA"

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
    # Ajout d'un champ temporaire pour permettre la migration
    code_interne = models.CharField(max_length=10, blank=True, null=True)  # Champ temporaire

    def __str__(self):
        return f"Paiement de {self.montant} FCFA effectué via {self.get_type_paiement_display()} le {self.date_payement.strftime('%d-%m-%Y')}"

class Statistique(models.Model):
    def calculerVente(self):
        ventes = Vente.objects.all()
        total_ventes = sum(vente.montant_total for vente in ventes)
        return total_ventes

    # Pas besoin de modification ici
    def __str__(self):
        return f"Statistique des ventes"
