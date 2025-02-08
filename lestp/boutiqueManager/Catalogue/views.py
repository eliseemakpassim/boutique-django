from django.shortcuts import render,redirect
from .forms import ProduitForm, CategorieForm
from .models import Produit, Categorie
# Create your views here.


# Vue pour la page d'accueil
def home(request):
    return render(request, 'home.html')



#  methode pour afficher la liste des produits
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'Catalogue/liste_produits.html', {'produits': produits})

#  methode pour ajouter un produit
def ajouter_produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            nom = form.cleaned_data['nom']
            description = form.cleaned_data['description']
            prix = form.cleaned_data['prix']
            quantite = form.cleaned_data['quantite']
            categorie_nom = form.cleaned_data['categorie']

            # Vérifier si la catégorie existe déjà
            categorie, created = Categorie.objects.get_or_create(nom=categorie_nom)

            # Enregistrer le produit
            Produit.objects.create(nom=nom, description=description, prix=prix, quantite=quantite, categorie=categorie)
            return redirect('liste_produits')

    else:
        form = ProduitForm()

    return render(request, 'Catalogue/ajouter_produit.html', {'form': form})

#  Afficher la liste des catégories
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'Catalogue/liste_categories.html', {'categories': categories})

#  Ajouter une catégorie
def ajouter_categorie(request):
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            nom_categorie = form.cleaned_data['nom']  # Récupérer le nom

            # Vérifier si la catégorie existe déjà
            if not Categorie.objects.filter(nom=nom_categorie).exists():
                Categorie.objects.create(nom=nom_categorie)  # Enregistrer la catégorie
                return redirect('liste_categories')  # Rediriger vers la liste des catégories
            else:
                form.add_error('nom', 'Cette catégorie existe déjà.')  # Ajouter une erreur si elle existe déjà
        
    else:
        form = CategorieForm()

    return render(request, 'Catalogue/ajouter_categorie.html', {'form': form})

