from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),  # Page d'accueil
     
    #urls de l'application Catalogue
    
    #  urls de l'affichage la liste des produits
    path('produits/', views.liste_produits, name='liste_produits'),
    #  urls de l'ajout d'un produit
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    
    
    #urls de l'application Catalogue
    
    #  urls de l'affichage la liste des catégories
    path('categories/', views.liste_categories, name='liste_categories'),
    #  urls de l'ajout d'une catégorie
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
]
