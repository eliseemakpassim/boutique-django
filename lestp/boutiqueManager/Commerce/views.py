from django.shortcuts import render, redirect, get_object_or_404
from .models import Panier, Vente, MobileMoney
from .forms import PanierForm, VenteForm, MobileMoneyForm
# Create your views here.


def liste_paniers(request):
    paniers = Panier.objects.all()
    return render(request, 'Commerce/liste_paniers.html', {'paniers': paniers})

def liste_ventes(request):
    ventes = Vente.objects.all()
    return render(request, 'Commerce/liste_ventes.html', {'ventes': ventes})

def liste_paiements(request):
    paiements = MobileMoney.objects.all()
    return render(request, 'Commerce/liste_paiements.html', {'paiements': paiements})


def ajouter_panier(request):
    if request.method == "POST":
        form = PanierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Commerce:liste_paniers')  # Change ceci selon ton URL
    else:
        form = PanierForm()
    return render(request, 'Commerce/ajouter_panier.html', {'form': form})

def ajouter_vente(request):
    if request.method == "POST":
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Commerce:liste_ventes')  # Change ceci selon ton URL
    else:
        form = VenteForm()
    return render(request, 'Commerce/ajouter_vente.html', {'form': form})

def ajouter_paiement(request):
    if request.method == "POST":
        form = MobileMoneyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Commerce:liste_paiements')  # Change ceci selon ton URL
    else:
        form = MobileMoneyForm()
    return render(request, 'Commerce/ajouter_paiement.html', {'form': form})

# Modifier une vente
def modifier_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    if request.method == 'POST':
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('Commerce:liste_ventes')
    else:
        form = VenteForm(instance=vente)
    return render(request, 'Commerce/modifier_vente.html', {'form': form})

# Supprimer une vente
def supprimer_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    if request.method == 'POST':
        vente.delete()
        return redirect('Commerce:liste_ventes')  # Redirection vers la liste des ventes
    return render(request, 'Commerce/supprimer_vente.html', {'vente': vente})


# Modifier un paiement
def modifier_paiement(request, paiement_id):
    paiement = get_object_or_404(MobileMoney, id=paiement_id)
    if request.method == 'POST':
        form = MobileMoneyForm(request.POST, instance=paiement)
        if form.is_valid():
            form.save()
            return redirect('Commerce:liste_paiements')
    else:
        form = MobileMoneyForm(instance=paiement)
    return render(request, 'Commerce/modifier_paiement.html', {'form': form})

# Supprimer un paiement
def supprimer_paiement(request, paiement_id):
    paiement = get_object_or_404(MobileMoney, id=paiement_id)
    if request.method == 'POST':
        paiement.delete()
        return redirect('Commerce:liste_paiements')  # Redirection vers la liste des paiements
    return render(request, 'Commerce/supprimer_paiement.html', {'paiement': paiement})

# Modifier un panier
def modifier_panier(request, panier_id):
    panier = get_object_or_404(Panier, id=panier_id)
    if request.method == 'POST':
        form = PanierForm(request.POST, instance=panier)
        if form.is_valid():
            form.save()
            return redirect('Commerce:liste_paniers')
    else:
        form = PanierForm(instance=panier)
    return render(request, 'Commerce/modifier_panier.html', {'form': form})

# Supprimer un panier
def supprimer_panier(request, panier_id):
    panier = get_object_or_404(Panier, id=panier_id)
    if request.method == 'POST':
        panier.delete()
        return redirect('Commerce:liste_paniers')  # Redirection vers la liste des paniers
    return render(request, 'Commerce/supprimer_panier.html', {'panier': panier})

