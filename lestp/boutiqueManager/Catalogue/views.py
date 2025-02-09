from django.shortcuts import render,redirect,get_object_or_404
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

#  Afficher les produits d'une catégorie
def categorie_produits(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    produits = Produit.objects.filter(categorie=categorie)
    return render(request, 'Catalogue/produits_par_categorie.html', {'categorie': categorie, 'produits': produits})

# methode  pour modifier un produit
def modifier_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            # Rediriger vers la liste des produits
            return redirect('liste_produits')  
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'Catalogue/modifier_produit.html', {'form': form, 'produit': produit})

# methode pour modifier une categorie
def modifier_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)

    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()  # Enregistre les modifications dans la base de données
            return redirect('liste_categories')  # Redirige vers la liste des catégories
    else:
        form = CategorieForm(instance=categorie)

    return render(request, 'Catalogue/modifier_categorie.html', {'form': form, 'categorie': categorie})

#methode pour supprimer une categorie

def supprimer_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')  # redirige vers la liste des catégories
    return render(request, 'Catalogue/supprimer_categorie.html', {'categorie': categorie})


#methode pour supprimer un produit
def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')  # Redirige vers la liste des produits
    return render(request, 'Catalogue/supprimer_produit.html', {'produit': produit})




