from django.urls import path
from . import views
app_name = 'Commerce'

urlpatterns = [
    
    #liste des urls de l'application Commerce
    
     #urls pour la liste de paniers
    path('paniers/', views.liste_paniers, name='liste_paniers'),
    #urls pour la liste de ventes
    path('ventes/', views.liste_ventes, name='liste_ventes'),
    #urls pour la liste de paiements mobiles
    path('paiements/', views.liste_paiements, name='liste_paiements'),
   
    #urls pour l'ajout d'un panier
    path('panier/ajouter/', views.ajouter_panier, name='ajouter_panier'),
    #urls pour l'ajout d'une vente
    path('vente/ajouter/', views.ajouter_vente, name='ajouter_vente'),
    #urls pour l'ajout d'un paiement mobile
    path('paiement/ajouter/', views.ajouter_paiement, name='ajouter_paiement'),
    
    # Panier
    #urls pour la modification d'un panier
    path('panier/modifier/<int:panier_id>/', views.modifier_panier, name='modifier_panier'),
    #urls pour la suppression d'un panier
    path('panier/supprimer/<int:panier_id>/', views.supprimer_panier, name='supprimer_panier'),
    
    # Vente
    #urls pour la modification d'une vente
    path('vente/modifier/<int:vente_id>/', views.modifier_vente, name='modifier_vente'),
    #urls pour la suppression d'une vente
    path('vente/supprimer/<int:vente_id>/', views.supprimer_vente, name='supprimer_vente'),
    
    # Paiement (MobileMoney)
    #urls pour la modification d'un paiement
    path('paiement/modifier/<int:paiement_id>/', views.modifier_paiement, name='modifier_paiement'),
    #urls pour la suppression d'un paiement
    path('paiement/supprimer/<int:paiement_id>/', views.supprimer_paiement, name='supprimer_paiement'),

    
]
