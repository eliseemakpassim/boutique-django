from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),  # Page d'accueil
     
    #urls de l'application Catalogue
    
    #  urls de l'affichage la liste des produits
    path('produits/', views.liste_produits, name='liste_produits'),
    #  urls de l'ajout d'un produit
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    #  urls de l'affichage la liste des catégories
    path('categories/', views.liste_categories, name='liste_categories'),
    #  urls de l'ajout d'une catégorie
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    #  urls de l'affichage la liste des produits d'une catégorie
    path('categorie/<int:id>/produits/', views.categorie_produits, name='produits_par_categorie'),
    # urls pour la modification d'un produit
    path('produit/<int:id>/modifier/', views.modifier_produit, name='modifier_produit'),
    #urls pour la modification d'une catégorie
     path('categorie/<int:id>/modifier/', views.modifier_categorie, name='modifier_categorie'),
    # urls pour la suppression d'un produit
    path('produit/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    # urls pour la suppression d'une catégorie
     path('categorie/supprimer/<int:categorie_id>/', views.supprimer_categorie, name='supprimer_categorie'),
    
    
    #urls de l'application Catalogue
    
    
]
