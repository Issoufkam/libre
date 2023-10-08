from django.db import models
from django.contrib.auth.models import User

class Coursier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    solde_compte = models.DecimalField(max_digits=10, decimal_places=2)
    numero = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username

class RechargeTransaction(models.Model):
    coursier = models.ForeignKey(Coursier, on_delete=models.CASCADE)
    montant = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Montant de la recharge en FCFA."
    )
    numero_compte_a_debiter = models.CharField(
        max_length=20,
        help_text="Numéro de compte à débiter."
    )

    # Choix pour le type de mobile money
    TYPE_MOBILE_MONEY_CHOICES = (
        ('Orange', 'Orange Money'),
        ('MTN', 'MTN Mobile Money'),
        ('Moov', 'Moov Money'),
        ('Wave', 'Wave Money'),
    )

    type_mobile_money = models.CharField(
        max_length=10,
        choices=TYPE_MOBILE_MONEY_CHOICES,
        help_text="Type de Mobile Money pour la recharge."
    )
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Transaction de {self.montant} FCFA par {self.coursier.user.username} le {self.date}"
