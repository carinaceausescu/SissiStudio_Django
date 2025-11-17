from django.db import models
import uuid

class Categorie(models.Model):
    nume = models.CharField(max_length=100, unique = True)
    icon = models.ImageField(upload_to='categorii_icon/', blank=True, null=True)
    def __str__(self):
        return self.nume
    

class Articol(models.Model):
    nume = models.CharField(max_length=100)
    pret = models.DecimalField(max_digits=8, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    imagine = models.ImageField(upload_to='produse/', null=True, blank=True)
    marimi = models.ManyToManyField('Marime', through='MarimeArticol')
    def __str__(self):
        return self.nume
    
TIP_MARIME = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
]
    
class Marime(models.Model):
    nume = models.CharField(max_length=50, choices=TIP_MARIME)
    descriere = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nume
    
class MarimeArticol(models.Model):
    marime = models.ForeignKey('Marime', on_delete=models.CASCADE)
    articol = models.ForeignKey('Articol', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('marime', 'articol')



class VanzariZilnice(models.Model):
    data = models.DateField(auto_now_add=True)
    cantitate = models.IntegerField()
    venit_total = models.IntegerField()
    articol = models.ForeignKey(Articol, on_delete=models.CASCADE)
    def __str__(self):
        return f"VanzariZilnice {self.id} - Articol: {self.articol.nume} - Data: {self.data}"
    
class Depozit(models.Model):
    nume = models.CharField(max_length=200)
    adresa = models.TextField()
    oras = models.CharField(max_length=200)
    activ = models.BooleanField(default=True)
    def __str__(self):
        return self.nume
    
class Stoc(models.Model):
    cantitate = models.IntegerField()
    actualizat = models.DateTimeField(auto_now=True)
    articol = models.ForeignKey(Articol, on_delete=models.CASCADE)
    depozit = models.ForeignKey(Depozit, on_delete=models.CASCADE)
    def __str__(self):
        return f"Stoc {self.id} - Articol: {self.articol.nume} - Cantitate: {self.cantitate}"    

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telefon = models.CharField(max_length=15, blank=True)
    data_nasterii = models.DateField(null=True, blank=True)
    adresa_livrare = models.TextField(blank=True, null=True)
    abonat_newsletter = models.BooleanField(default=False)
    data_inregistrare = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.username} ({self.email})"
