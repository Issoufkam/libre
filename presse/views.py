from django.shortcuts import render, redirect
from .forms import RechargeForm
from django.contrib.auth.models import User  # Importez le modèle d'utilisateur Django
from django.urls import reverse

# Vue pour la page d'accueil
def home(request):
    return render(request, 'home.html')

# Vue pour le rechargement du compte
def recharge_compte(request):
    if request.method == 'POST':
        form = RechargeForm(request.POST)
        if form.is_valid():
            nom_utilisateur = form.cleaned_data['nom_utilisateur']
            montant = form.cleaned_data['montant']
            numero_compte_a_debiter = form.cleaned_data['numero_compte_a_debiter']
            type_mobile_money = form.cleaned_data['type_mobile_money']

            # Recherchez l'utilisateur dans la base de données
            try:
                utilisateur = User.objects.get(username=nom_utilisateur)
            except User.DoesNotExist:
                # Si l'utilisateur n'existe pas, renvoyez un message d'erreur
                message_erreur = "Nom d'utilisateur invalide. Veuillez vérifier et réessayer."
                return render(request, 'echec.html', {'message': message_erreur})

            # Continuez avec le traitement de la recharge ici
            # Assurez-vous de vérifier le solde de l'utilisateur et d'autres validations

            # Redirigez vers la page de confirmation en passant les détails de la recharge dans l'URL
            confirmation_url = reverse('confirmation_recharge')
            confirmation_url += f'?nom_utilisateur={nom_utilisateur}&montant={montant}&numero_compte_a_debiter={numero_compte_a_debiter}&type_mobile_money={type_mobile_money}'
            return redirect(confirmation_url)

        # En cas d'échec de la validation du formulaire, affichez-le à nouveau avec des erreurs
        return render(request, 'recharge.html', {'form': form})

    # Si la méthode HTTP n'est pas POST, affichez simplement le formulaire vide
    form = RechargeForm()
    return render(request, 'recharge.html', {'form': form})

# Vue pour la confirmation de recharge
def confirmation_recharge(request):
    # Récupérez les informations de la recharge depuis les paramètres d'URL
    nom_utilisateur = request.GET.get('nom_utilisateur', '')
    montant = request.GET.get('montant', '')
    numero_compte_a_debiter = request.GET.get('numero_compte_a_debiter', '')
    type_mobile_money = request.GET.get('type_mobile_money', '')

    context = {
        'nom_utilisateur': nom_utilisateur,
        'montant': montant,
        'numero_compte_a_debiter': numero_compte_a_debiter,
        'type_mobile_money': type_mobile_money,
    }

    return render(request, 'confirmation_recharge.html', context)

# Vue pour l'échec de recharge
def echec_recharge(request, message):
    context = {
        'message': message,
    }
    return render(request, 'echec.html', context)
