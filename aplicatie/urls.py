from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("despre/", views.despre, name="despre"),
    path("contact/", views.contact, name="contact"),
    path("cos_virtual/", views.in_lucru, name="cos_virtual"),   
    path("produse/", views.produse, name="produse"), 
    path('produse/<int:id>/', views.detalii_produs, name='detalii_produs'),
    path("categorii/<str:categorie_nume>/", views.categorie, name="categorie"),
    path("adauga_articol/", views.adauga_articol, name="adauga_articol"), 
    path("info/", views.info, name="info"),
    path("log/", views.log, name="log"),
    #path('trimite_emai/', views.trimite_email, name='trimite_email'),
    #path('inregistrare/', views.inregistrare, name='inregistrare'),
    #path('login/', views.login_view, name='login'),
    #path('profil/', views.profil, name='profil'),
    #path('logout/', views.logout_view, name='logout'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
