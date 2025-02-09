from django import forms
from .models import Panier, Vente, MobileMoney, Produit

class PanierForm(forms.ModelForm):
    produits = forms.ModelMultipleChoiceField(
        queryset=Produit.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Produits dans le panier"
    )

    class Meta:
        model = Panier
        fields = ['produits', 'nombre_de_produits']
        labels = {
            'nombre_de_produits': 'Nombre total de produits',
        }
        widgets = {
            'nombre_de_produits': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }

class VenteForm(forms.ModelForm):
    produits = forms.ModelMultipleChoiceField(
        queryset=Produit.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Produits vendus"
    )

    class Meta:
        model = Vente
        fields = ['produits', 'quantite', 'montant_total']
        labels = {
            'quantite': 'Quantité vendue',
            'montant_total': 'Montant total',
        }
        widgets = {
            'quantite': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
            'montant_total': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'class': 'form-control'}),
        }

class MobileMoneyForm(forms.ModelForm):
    class Meta:
        model = MobileMoney
        fields = ['montant', 'type_paiement']
        labels = {
            'montant': 'Montant du paiement',
            'type_paiement': 'Type de paiement',
        }
        widgets = {
            'montant': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'class': 'form-control'}),
            'type_paiement': forms.Select(attrs={'class': 'form-control'}),
        }