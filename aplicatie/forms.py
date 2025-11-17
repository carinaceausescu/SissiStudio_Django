from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import Categorie, Marime, CustomUser
from django.forms.widgets import CheckboxSelectMultiple


class FilterFormArticole(forms.Form):
    pret_minim = forms.DecimalField(
        required=False, 
        min_value=0, 
        decimal_places=2, 
        max_digits=10,
        widget=forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0'}),
    )
    pret_maxim = forms.DecimalField(
        required=False, 
        min_value=0, 
        decimal_places=2, 
        max_digits=4,
        widget=forms.NumberInput(attrs={'step': '0.01', 'placeholder': '999'}),
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(), 
        required=False, 
        empty_label="Toate categoriile",
        widget=forms.Select(),
    )
    marime = forms.ModelMultipleChoiceField(
        queryset=Marime.objects.all(), 
        required=False,
        widget=CheckboxSelectMultiple,
    )
    items_per_page = forms.IntegerField(
        required=False, 
        min_value=1,
        widget=forms.NumberInput(attrs = {'placeholder': '5'}),
    )
    
    def clean(self):
        cleaned_data = super().clean()
        pret_minim = cleaned_data.get('pret_minim')
        pret_maxim = cleaned_data.get('pret_maxim')
        categorie = cleaned_data.get('categorie')
        marime = cleaned_data.get('marime')
        items_per_page = cleaned_data.get('items_per_page') or 5

        if items_per_page in [None, '']:
            cleaned_data['items_per_page'] = 5
            items_per_page = 5

        if pret_minim is not None and pret_maxim is not None:
            if pret_maxim < pret_minim:
                self.add_error('pret_maxim', 'Pretul maxim trebuie sa fie mai mare sau egal cu pretul minim!')

        if items_per_page == 0:
            self.add_error('items_per_page', 'Numarul de articole pe pagină trebuie sa fie mai mare decat 0!')
            
        if items_per_page in [None, '']:
            items_per_page = 5

        if not (pret_minim or pret_maxim or categorie or (marime and len(marime) > 0)):
            raise forms.ValidationError('Trebuie sa selectezi cel putin un filtru pentru a da submit!')
        
        return cleaned_data

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    mesaj = forms.CharField(widget=forms.Textarea, required=True)


class CustomUserCreationForm(UserCreationForm):
    telefon = forms.CharField(required=False)
    data_nasterii = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    adresa_livrare = forms.CharField(widget=forms.Textarea, required=False)
    abonat_newsletter = forms.BooleanField(required=False, initial=False)
    data_inregistrare = forms.DateTimeField(widget=forms.HiddenInput(), initial=date.today)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "telefon", "data_nasterii", "adresa_livrare", "abonat_newsletter", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.telefon = self.cleaned_data.get("telefon")
        user.data_nasterii = self.cleaned_data.get("data_nasterii")
        user.adresa_livrare = self.cleaned_data.get("adresa_livrare")
        user.abonat_newsletter = self.cleaned_data.get("abonat_newsletter")
        # data_inregistrare is auto-set in model; keep if passed
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator', max_length=150)
    password = forms.CharField(label='Parola', widget=forms.PasswordInput)
    ramane_logat = forms.BooleanField(label='Tine-ma minte 1 zi', required=False)
