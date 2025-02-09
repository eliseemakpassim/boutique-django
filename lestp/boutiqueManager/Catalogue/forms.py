from django import forms
from .models import Produit, Categorie

# Formulaire pour ajouter ou modifier une catégorie
class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie  
        fields = ['nom']  
        labels = {
            'nom': 'Nom de la catégorie',
        }

# Formulaire pour ajouter ou modifier un produit
class ProduitForm(forms.ModelForm):
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        empty_label="Sélectionnez une catégorie",
        label="Catégorie",
        widget=forms.Select(attrs={'class': 'form-control'}),  # Ajout de style (optionnel)
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categorie'].label_from_instance = lambda obj: obj.nom  # Afficher le nom de la catégorie

    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'quantite', 'categorie']  
        labels = {
            'nom': 'Nom du produit',
            'description': 'Description',
            'prix': 'Prix',
            'quantite': 'Quantité',
            'categorie': 'Catégorie',
        }

    # Validation personnalisée pour le prix
    def clean_prix(self):
        prix = self.cleaned_data.get('prix')
        if prix <= 0:
            raise forms.ValidationError("Le prix doit être supérieur à 0.")
        return prix
