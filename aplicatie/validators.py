from django.core.exceptions import ValidationError
from datetime import date
import re

def validate_major(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("Trebuie sa fii major (peste 18 ani).")

def validate_mesaj_length(value):
    words = re.findall(r'\b\w+\b', value)
    if not (5 <= len(words) <= 100):
        raise ValidationError("Mesajul trebuie sa aiba intre 5 si 100 de cuvinte.")
    for word in words:
        if len(word) > 15:
            raise ValidationError("Fiecare cuvant din mesaj nu poate depasi 15 caractere.")

def validate_no_links(value):
    for word in re.findall(r'\b\w+\b', value):
        if word.startswith("http://") or word.startswith("https://"):
            raise ValidationError("Textul nu poate contine linkuri.")

TIP_MESAJ_VALIDE = ['reclamatie', 'intrebare', 'review', 'cerere', 'programare']
def validate_tip_mesaj(value):
    if value not in TIP_MESAJ_VALIDE:
        raise ValidationError("Trebuie sa selectezi un tip valid de mesaj.")

def validate_cnp(value):
    if not value.isdigit():
        raise ValidationError("CNP-ul trebuie sa contina doar cifre.")
    if len(value) != 13:
        raise ValidationError("CNP-ul trebuie sa aiba exact 13 cifre.")
    if value[0] not in ('1', '2'):
        raise ValidationError("CNP-ul trebuie sa inceapa cu 1 sau 2.")
    yy, mm, dd = int(value[1:3]), int(value[3:5]), int(value[5:7])
    try:
        year = 1900 + yy
        date(year, mm, dd)
    except ValueError:
        raise ValidationError("CNP-ul trebuie sa contina o data valida in cifrele 2-7.")

TEMP_EMAIL_DOMAINS = ['guerillamail.com', 'yopmail.com']
def validate_email_not_temp(value):
    domain = value.split('@')[-1]
    if domain in TEMP_EMAIL_DOMAINS:
        raise ValidationError("Nu se accepta adrese de email temporare.")

def validate_start_upper_and_letters(value):
    if not value:
        return
    if not re.match(r'^[A-Z][A-Za-z\s-]*$', value):
        raise ValidationError("Trebuie sa inceapa cu litera mare si sa contina doar litere, spatii si cratima.")

def validate_upper_after_space_or_dash(value):
    for match in re.finditer(r'[\s-][a-zA-Z]', value):
        if not match.group()[1].isupper():
            raise ValidationError("Fiecare cuvant dupa spatiu sau cratima trebuie sa inceapa cu litera mare.")
