from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Categorie, Articol, Marime, MarimeArticol, VanzariZilnice, Depozit, Stoc, CustomUser
# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'icon')
    search_fields = ('nume',)

class ArticolAdmin(admin.ModelAdmin):
    list_display = ('nume', 'pret', 'categorie')
    list_filter = ('categorie',)
    ordering = ('-pret',)
    search_fields = ('nume',)
    list_per_page = 5
    fieldsets = (
        ('InformaTii Principale', {
            'fields': ('nume', 'pret')
        }),
        ('Informatii secundare', {
            'fields': ('categorie', 'imagine'),
            'classes': ('collapse',), 
        }),
    )
    
class MarimeAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere')
    search_fields = ('nume', 'descriere')

class MarimeArticolAdmin(admin.ModelAdmin):
    list_display = ('marime', 'articol')
    search_fields = ('marime__nume', 'articol__nume')
    
class VanzariZilniceAdmin(admin.ModelAdmin):
    list_display = ('data', 'cantitate', 'venit_total', 'articol')
    ordering = ('data',)
    search_fields = ('articol__nume', 'data')
    
class DepozitAdmin(admin.ModelAdmin):
    list_display = ('nume', 'oras', 'activ')
    search_fields = ('nume', 'oras')

class StocAdmin(admin.ModelAdmin):
    list_display = ('articol', 'depozit', 'cantitate', 'actualizat')
    search_fields = ('articol__nume', 'depozit__nume')
    
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Articol, ArticolAdmin)
admin.site.register(Marime, MarimeAdmin)
admin.site.register(MarimeArticol, MarimeArticolAdmin)
admin.site.register(VanzariZilnice, VanzariZilniceAdmin)
admin.site.register(Depozit, DepozitAdmin)
admin.site.register(Stoc, StocAdmin)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'telefon', 'data_nasterii', 'abonat_newsletter', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefon', 'data_nasterii', 'adresa_livrare', 'abonat_newsletter', 'data_inregistrare')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_header = "Pagina gestionare baza de date"
admin.site.site_title = "Admin Site"
admin.site.index_title = "Bine ai venit in pagina admin a site-ului Sissi Studio!"
