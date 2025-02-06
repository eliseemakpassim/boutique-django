from django import forms
from .models import Produit, Categorie

class CategorieForm(forms.Form):
    nom = forms.CharField(label="Nom de la catégorie", max_length=100)
    
    
class ProduitForm(forms.Form):
    nom = forms.CharField(label="Nom du produit", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    prix = forms.DecimalField(label="Prix", min_value=0, max_digits=10, decimal_places=2)
    quantite = forms.IntegerField(label="Quantité", min_value=0)
    categorie = forms.CharField(label="Catégorie", max_length=100) 
    



 