from .models import Categorie

def categorii(request):
    categorii = Categorie.objects.all()
    return {
        'categorii': categorii
    }