from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import Categorie, Marime, Articol, CustomUser
from django.forms.widgets import CheckboxSelectMultiple
import re


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
        max_digits=10,
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
        
        return cleaned_data
    
    

def validate_major(data_nasterii):
    if not data_nasterii:
        return
    azi = date.today()
    varsta = azi.year - data_nasterii.year - ((azi.month, azi.day) < (data_nasterii.month, data_nasterii.day))
    if varsta < 18:
        raise ValidationError("Trebuie sa ai cel putin 18 ani pentru a trimite mesajul.")


def validate_no_links(value):
    if re.search(r'\bhttps?://', value):
        raise ValidationError("Textul nu poate contine linkuri.")


def validate_message_length(value):
    words = re.findall(r'\b\w+\b', value)
    if not (5 <= len(words) <= 100):
        raise ValidationError("Mesajul trebuie sa contina intre 5 si 100 de cuvinte.")
    for w in words:
        if len(w) > 15:
            raise ValidationError("Fiecare cuvant din mesaj nu poate avea mai mult de 15 caractere.")


def validate_capitalized_text(value):
    if not value:
        return
    if not re.fullmatch(r'[A-Z][A-Za-z -]*', value):
        raise ValidationError("Trebuie sa inceapa cu litera mare si sa contina doar litere, spatii sau cratima.")


def validate_name_words_capital(value):
    if not value:
        return
    for w in re.split(r'[\s-]', value):
        if w and not w[0].isupper():
            raise ValidationError("Fiecare cuvant trebuie sa inceapa cu litera mare.")


def validate_cnp(value):
    if not value:
        return
    if not re.fullmatch(r'\d{13}', value):
        raise ValidationError("CNP-ul trebuie sa contina exact 13 cifre.")
    if value[0] not in ['1','2','5','6']:
        raise ValidationError("CNP-ul trebuie sa inceapa cu 1, 2, 5 sau 6.")
    yy = int(value[1:3])
    mm = int(value[3:5])
    dd = int(value[5:7])
    
    secol = 1900 if value[0]=='1' else 2000
    try:
        date(secol+yy, mm, dd)
    except ValueError:
        raise ValidationError("CNP-ul contine o data invalida.")


def validate_email_domain(value):
    forbidden = ['guerillamail.com', 'yopmail.com']
    domain = value.split('@')[-1].lower()
    if domain in forbidden:
        raise ValidationError(f"Email-ul nu poate avea domeniul {domain}.")


class ContactForm(forms.Form):
    TIP_MESAJ = [
        ('', 'Neselectat'),
        ('reclamatie', 'Reclamatie'),
        ('intrebare', 'Intrebare'),
        ('review', 'Review'),
        ('cerere', 'Cerere'),
        ('programare', 'Programare'),
    ]
    nume = forms.CharField(
        max_length=100, 
        required=True,
        label="Nume*",
        validators=[validate_capitalized_text, validate_name_words_capital],
    )
    prenume = forms.CharField(
        max_length=10,
        required=False,
        label="Prenume",
        validators=[validate_capitalized_text, validate_name_words_capital],
    )
    cnp = forms.CharField(
        min_length=13,
        max_length=13,
        required=False,
        label="CNP",
        validators=[validate_cnp],
    )
    data_nasterii = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data nasterii*",
        validators=[validate_major],
    )
    email = forms.EmailField(
        required=True,
        label="E-mail*",
        validators=[validate_email_domain],
    )
    email_confirmare = forms.EmailField(
        required=True,
        label="Confirmare e-mail*",
    )
    tip_mesaj = forms.ChoiceField(
        choices=TIP_MESAJ,
        required=True,
        label="Tip mesaj*",
        initial="",
    )
    subiect = forms.CharField(
        max_length=100,
        required=True,
        label="Subiect*",
        validators=[validate_capitalized_text],
    )
    minim_zile_asteptare = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=30,
        label="Minim zile de asteptare (Pentru review-uri/cereri minimul de zile de asteptare trebuie setat de la 4 incolo iar pentru cereri/intrebari de la 2 incolo. Maximul e 30.)*",
    )
    mesaj = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Mesaj",
        validators=[validate_no_links, validate_message_length],
    )
    def clean(self):
        cleaned = super().clean()

        nume = cleaned.get("nume")
        email = cleaned.get("email")
        email_confirmare = cleaned.get("email_confirmare")
        mesaj = cleaned.get("mesaj")
        tip_mesaj = cleaned.get("tip_mesaj")
        minim_zile_asteptare = cleaned.get("minim_zile_asteptare")
        cnp = cleaned.get("cnp")
        data_nasterii = cleaned.get("data_nasterii")

        if email and email_confirmare and email != email_confirmare:
            raise ValidationError("Emailul si confirmarea trebuie sa coincida.")

        if mesaj and nume:
            ultimul_cuv = mesaj.strip().split()[-1]
            if ultimul_cuv.lower() != nume.lower():
                raise ValidationError("Mesajul trebuie sa se incheie cu numele tau (semnatura).")


        if cnp and len(cnp) == 13 and data_nasterii:
            an = int(cnp[1:3])
            luna = int(cnp[3:5])
            zi = int(cnp[5:7])

            s = cnp[0]
            if s in ["1", "2"]:
                an += 1900
            elif s in ["5", "6"]:
                an += 2000

            if date(an, luna, zi) != data_nasterii:
                raise ValidationError("CNP-ul nu corespunde cu data nasterii introdusa.")

        if tip_mesaj and minim_zile_asteptare is not None:
            if tip_mesaj in ["review", "cerere"] and minim_zile_asteptare < 4:
                self.add_error(
                    "minim_zile_asteptare",
                    "Pentru review-uri si cereri trebuie minim 4 zile."
                )

            if tip_mesaj in ["cerere", "intrebare"] and minim_zile_asteptare < 2:
                self.add_error(
                    "minim_zile_asteptare",
                    "Pentru cereri si intrebari trebuie minim 2 zile."
                )

        if data_nasterii:
            azi = date.today()
            ani = azi.year - data_nasterii.year
            luni = azi.month - data_nasterii.month
            if azi.day < data_nasterii.day:
                luni -= 1
            if luni < 0:
                ani -= 1
                luni += 12
            cleaned["data_nasterii"] = f"{ani} ani si {luni} luni"

        if mesaj:
            mesaj = mesaj.replace("\n", " ")
            mesaj = re.sub(r"\s+", " ", mesaj).strip()
            
            def capitalize_after_punctuation(text):
                def repl(m):
                    punct = m.group(1)
                    lit = m.group(2).upper()
                    return punct + " " + lit
                text = text.strip()
                text = re.sub(
                    r"(\.\.\.)(\s*[a-zA-Z])", 
                    lambda m: m.group(1) + " " + m.group(2).strip().upper(),
                    text
                )
                text = re.sub(r"([\.!?])\s*([a-zA-Z])", repl, text)
                return text

            mesaj = capitalize_after_punctuation(mesaj)
            cleaned["mesaj"] = mesaj

        urgent = False
        if tip_mesaj and minim_zile_asteptare is not None:
            if (tip_mesaj in ["review", "cerere"] and minim_zile_asteptare == 4) or (tip_mesaj in ["cerere", "intrebare"] and minim_zile_asteptare == 2):
                urgent = True

        cleaned["urgent"] = urgent

        return cleaned

def validate_min_two_words(value):
    if len(value.strip().split()) < 2:
        raise ValidationError("Numele trebuie sa contina minim doua cuvinte.")

class ArticolForm(forms.ModelForm):
    cost_import = forms.DecimalField(
        max_digits=8, 
        decimal_places=2,
        required=True,
        label="Cost de cumparare import"
    )
    procent_adaugat = forms.IntegerField(
        min_value=0,
        max_value=100,
        required=True,
        label="Procent adaugat",
        help_text="Procentul trebuie sa fie multiplu de 5."
    )
    class Meta:
        model = Articol
        fields = ["nume", "categorie", "imagine"]
        labels = {
            "nume": "Denumirea articolului",
            "categorie": "Categoria",
            "imagine": "Imaginea cu articolul"
        }
        help_texts = {
            "imagine": "Incarca o poza clara cu articolul.",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nume'].validators.extend([validate_capitalized_text, validate_min_two_words])
    
    def clean_nume(self):
        nume = self.cleaned_data.get("nume")
        if Articol.objects.filter(nume__iexact=nume).exists():
            raise forms.ValidationError("Exista deja un articol vestimentar cu aceasta denumire.")
        return nume
    def clean_procent_adaugat(self):
        procent = self.cleaned_data.get("procent_adaugat")
        if procent % 5 != 0:
            raise forms.ValidationError("Procentul adaugat trebuie sa fie multiplu de 5.")
        return procent
    def clean_cost_import(self):
        cost = self.cleaned_data.get("cost_import")
        if cost <= 0:
            raise forms.ValidationError("Costul de cumparare trebuie sa fie strict pozitiv.")  
        return cost
    def clean(self):
        cleaned_data = super().clean()
        nume = cleaned_data.get("nume")
        categorie = cleaned_data.get("categorie")
        if nume and categorie:
            first4nume = nume[:4].lower()
            first4categorie = categorie.nume[:4].lower()
            if first4nume != first4categorie:
                raise forms.ValidationError("Articolul nu face parte din categoria aleasa.")
        return cleaned_data

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
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator', max_length=150)
    password = forms.CharField(label='Parola', widget=forms.PasswordInput)
    ramane_logat = forms.BooleanField(label='Tine-ma minte 1 zi', required=False)
