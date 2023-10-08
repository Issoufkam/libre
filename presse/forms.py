from django import forms

class RechargeForm(forms.Form):
    nom_utilisateur = forms.CharField(label="Nom d'utilisateur", max_length=100)
    montant = forms.DecimalField(label="Montant", max_digits=10, decimal_places=2)
    numero_compte_a_debiter = forms.CharField(label="Numéro de compte à débiter", max_length=20)

    
    TYPE_MOBILE_MONEY_CHOICES = (
        ('Orange', 'Orange Money'),
        ('MTN', 'MTN Mobile Money'),
        ('Moov', 'Moov Money'),
        ('Wave', 'Wave Money'),
    )

    type_mobile_money = forms.ChoiceField(label="Type de Mobile Money", choices=TYPE_MOBILE_MONEY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(RechargeForm, self).__init__(*args, **kwargs)
        
        # En fonction du préfixe du "Numéro de compte à débiter", définissez les choix pour le champ "Type de Mobile Money"
        if 'numero_compte_a_debiter' in self.data:
            numero_compte_a_debiter = self.data['numero_compte_a_debiter']
            if numero_compte_a_debiter.startswith('07'):
                self.fields['type_mobile_money'].choices = [
                    ('Orange', 'Orange Money'),
                    ('Wave', 'Wave Money'),
                ]
            elif numero_compte_a_debiter.startswith('05'):
                self.fields['type_mobile_money'].choices = [
                    ('MTN', 'MTN Mobile Money'),
                    ('Wave', 'Wave Money'),
                ]
            elif numero_compte_a_debiter.startswith('01'):
                self.fields['type_mobile_money'].choices = [
                    ('Moov', 'Moov Money'),
                    ('Wave', 'Wave Money'),
                ]
            else:
                self.fields['type_mobile_money'].choices = self.TYPE_MOBILE_MONEY_CHOICES
        else:
            self.fields['type_mobile_money'].choices = self.TYPE_MOBILE_MONEY_CHOICES

    def clean_numero_compte_a_debiter(self):
        numero_compte_a_debiter = self.cleaned_data['numero_compte_a_debiter']
        
        # Vérifiez si le numéro de compte a exactement 10 chiffres
        if not numero_compte_a_debiter.isdigit() or len(numero_compte_a_debiter) != 10:
            raise forms.ValidationError("Le numéro de compte à débiter doit contenir exactement 10 chiffres.")
        
        return numero_compte_a_debiter


    type_mobile_money = forms.ChoiceField(label="Type de Mobile Money", choices=TYPE_MOBILE_MONEY_CHOICES)
