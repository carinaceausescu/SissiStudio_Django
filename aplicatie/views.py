from django.shortcuts import render, redirect
import datetime
from urllib.parse import urlparse
from django.http import HttpResponse, JsonResponse
from .forms import FilterFormArticole, ContactForm
from .models import Articol, Categorie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from django.urls import reverse
import json
import os
import time
from django.conf import settings
#from django.contrib.auth import authenticate, login
#from .forms import LoginForm


lista_accesari = []

def pag1(request):
    return HttpResponse(2+3)

l=[]
def pag2(request):
    global l
    a=request.GET.get("a",10)
    print(request.GET)
    l.append(a)
    return HttpResponse(f"<b>Am primit</b>: {l}")

def get_ip(request):
    req_headers = request.META
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[-1].strip()
    else:
        return request.META.get('REMOTE_ADDR')
    
def info(request):
    param_data = request.GET.get("data", None) 

    param = request.GET.keys()
    nr_param = len(param)
    nume_param = ", ".join(param) if nr_param > 0 else "niciunul"

    sectiune_parametri = f"""
    <section>
        <h2>Parametri</h2>
        <p>Numar parametri: {nr_param}</p>
        <p>Nume parametri: {nume_param}</p>
    </section>
    """
    
    sectiune_data = ""
    if param_data:
        sectiune_data = afis_data(param_data)
    else:
        sectiune_data = afis_data()

    continut = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <title>Informatii despre server</title>
    </head>
    <body>
        <h1>Informatii despre server</h1>
        {sectiune_data}
        {sectiune_parametri}
    </body>
    </html>
    """
    return render(request, 'aplicatie/baza.html', {'continut_custom': continut})

def afis_data(param='toate'):
    zile_sapt = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
    luni_an = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie",
            "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
    
    now = datetime.datetime.now()
    zi_sapt = zile_sapt[now.weekday()]        
    zi_luna = now.day
    luna = luni_an[now.month - 1]
    an = now.year
    ora = now.strftime("%H:%M:%S")

    if param.lower() == "zi":
        continut = f"{zi_sapt}, {zi_luna} {luna} {an}"
    elif param.lower() == "timp":
        continut = f"{ora}"
    else:
        continut = f"{zi_sapt}, {zi_luna} {luna} {an}, {ora}"

    return f"""
    <section>
        <h2>Data si ora</h2>
        <p>{continut}</p>
    </section>
    """

def afis_template(request):
    return render(request,"aplicatie/exemplu.html",
        {
            "titlu_tab":"Titlu fereastra",
            "titlu_articol":"Titlu afisat",
            "continut_articol":"Continut text"
        }
    )
    
class Accesare:
    id_cnt = 1  

    def __init__(self, ip=None, url=None, data=None):
        self.id = Accesare.id_cnt
        Accesare.id_cnt += 1

        self.ip = ip
        self.url_complet = url
        self.data = data or datetime.datetime.now()

    def lista_parametri(self):
        param_list = [
            ("id", self.id),
            ("ip", self.ip),
            ("url", self.url_complet),
            ("data", self.data)
        ]
        return [(nume, valoare if valoare is not None else None) for nume, valoare in param_list]

    def url(self):
        return self.url_complet

    def data(self, format_string="%Y-%m-%d %H:%M:%S"):
        return self.data.strftime(format_string)

    def pagina(self):
        if not self.url_complet:
            return None
        parsed = urlparse(self.url_complet)
        return parsed.path
    

def log(request):
    global lista_accesari
    ultimele_p = request.GET.get('ultimele')
    accesari_p = request.GET.get('accesari')
    iduri_p = request.GET.getlist('iduri')
    dubluri_p = request.GET.get('dubluri', 'false').lower()
    tabel_p = request.GET.get('tabel')
    
    mesaj = ""
    accesari_afis = lista_accesari
    
    if iduri_p:
        iduri_finale = []
        for p in iduri_p:
            for id_str in p.split(','):
                id_str = id_str.strip()
                if id_str.isdigit():
                    id_int = int(id_str)
                    iduri_finale.append(id_int)
        if dubluri_p != "true":
            iduri_unice = []
            for id_int in iduri_finale:
                if id_int not in iduri_unice:
                    iduri_unice.append(id_int)
            iduri_finale = iduri_unice
                        
        accesari_afis = [acc for acc in lista_accesari if acc.id in iduri_finale]
        accesari_afis.sort(key = lambda acc: iduri_finale.index(acc.id))
    
    elif ultimele_p is not None:
        if not ultimele_p.isdigit():
            return HttpResponse("'ultimele' trebuie sa fie intreg")
        n = int(ultimele_p)
        total = len(lista_accesari)
        if n > total:
            accesari_afis = lista_accesari
            mesaj += f"<p style='color:red;'>Exista doar {total} accesarifata de {n} accesari cerute. </p>"
        else:
            accesari_afis = lista_accesari[-n:]
    
    else:
        accesari_afis = lista_accesari
        
    if accesari_p == "nr":
        mesaj += f"<p><b>Numar total de accesari:</b> {len(lista_accesari)}</p>"
    
    elif accesari_p == "detalii":
        mesaj += "<h3>Deatlii accesari:</h3><ul>"
        for acc in lista_accesari:
            mesaj += f"<li>{acc.data.strftime('%Y-%m-%d %H:%M:%S')}</li>"
        mesaj +="</ul>"
        
    if tabel_p:
        if tabel_p == "tot":
            coloane = ["id", "ip", "url_complet", "data"]
        else:
            coloane = [c.strip() for c in tabel_p.split(",")]
        continut = "<h2>Accesari in tabel</h2><table border='1' style='border-collapse:collapse;'>"
        continut += "<tr>" + "".join([f"<th>{c}</th>" for c in coloane]) + "</tr>"
        for acc in accesari_afis:
            valori = []
            for c in coloane:
                valoare = getattr(acc, c, "")
                if isinstance(valoare, datetime.datetime):
                    valoare = valoare.strftime('%Y-%m-%d %H:%M:%S')
                valori.append(str(valoare))
            continut += "<tr>" + "".join([f"<td>{v}</td>" for v in valori]) + "</tr>"
        continut += "</table>"
    
    else:
        continut = "<h2>Lista accesari</h2><ul>"
        for acc in accesari_afis:
            continut += f"<li>{acc.ip} - {acc.url_complet} - {acc.data.strftime('%Y-%m-%d %H:%M:%S')}</li>" 
        continut += "</ul>"

    continut += mesaj
    
    if lista_accesari:
        fr = {}
        for acc in lista_accesari:
            pg = acc.pagina() or acc.url_complet
            fr[pg] = fr.get(pg, 0) + 1
        most = max(fr, key = fr.get)
        least = min(fr, key = fr.get)  
        
        continut += f"""
        <hr>
        <h3> Statistici accesari </h3>
        <p> <b> Cea mai accesata pagina: </b> {most} ({fr[most]} accesari)</p>
        <p> <b> Cea mai putin accesata pagina: </b> {least} ({fr[least]} accesari)</p>
        """
    else:
        continut += "<p> Nu exista accesari inregistrate.</p>"
    
    return render(request, 'aplicatie/baza.html', {'continut_custom': continut})

def home(request):
    recomandari = Articol.objects.filter(id__in=[1, 11, 12])
    return render(request, 'aplicatie/home.html', {'recomandari': recomandari})

def despre(request):
    return render(request, 'aplicatie/despre.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .forms import FilterFormArticole
from .models import Articol

def produse(request, categorie_nume=None):
    
    cat = None
    if categorie_nume:
        try:
            cat = Categorie.objects.get(nume=categorie_nume)
        except Categorie.DoesNotExist:
            return render(request, 'aplicatie/eroare.html')

    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        sort = request.POST.get("sort", "nume") 
        form = FilterFormArticole(request.POST)
        if form.is_valid():
            categorie_post = form.cleaned_data.get('categorie')
            if cat and categorie_post != cat:
                return JsonResponse({
                    "status": "error",
                    "message": "Nu poti modifica categoria filtrului."
                })
                
            produse_qs = Articol.objects.all()

            pret_minim = form.cleaned_data.get('pret_minim')
            pret_maxim = form.cleaned_data.get('pret_maxim')
            categorie = form.cleaned_data.get('categorie')
            marimi = form.cleaned_data.get('marime')
            items_per_page = form.cleaned_data.get('items_per_page') or 5
            pagina_curenta = int(request.POST.get('pagina') or 1)

            #filtrele
            if pret_minim is not None:
                produse_qs = produse_qs.filter(pret__gte=pret_minim)
            if pret_maxim is not None:
                produse_qs = produse_qs.filter(pret__lte=pret_maxim)
            if categorie:
                produse_qs = produse_qs.filter(categorie=categorie)
            if marimi:
                produse_qs = produse_qs.filter(marimi__in=marimi).distinct()

            #sortare
            if sort == "a":
                produse_qs = produse_qs.order_by('pret')
            elif sort == "d":
                produse_qs = produse_qs.order_by('-pret')

            #paginare
            paginator = Paginator(produse_qs, items_per_page)
            try:
                page_obj = paginator.page(pagina_curenta)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            #JSON
            produse_data = [
                {
                    "id": p.id,
                    "nume": p.nume,
                    "pret": p.pret,
                    "categorie": p.categorie.nume,
                    "categorie_url": p.categorie.nume,
                    "categorie_icon": p.categorie.icon.url if p.categorie.icon else None,
                    "imagine": p.imagine.url if p.imagine else None
                }
                for p in page_obj
            ]

            return JsonResponse({
                "status": "success",
                "produse": produse_data,
                "pagination": {
                    "pagina_actuala": page_obj.number,
                    "total_pagini": paginator.num_pages,
                    "has_previous": page_obj.has_previous(),
                    "has_next": page_obj.has_next(),
                    "previous_page_number": page_obj.previous_page_number() if page_obj.has_previous() else None,
                    "next_page_number": page_obj.next_page_number() if page_obj.has_next() else None
                }
            })

        else:
            print("ERORI FORMULAR:", form.errors)
            return JsonResponse({"status": "error", "message": "Formular invalid"})

    sort = request.GET.get("sort", "nume") 
    form = FilterFormArticole()
    produse_qs = Articol.objects.all()
    items = 5
    mesajEroare = None

    if sort == "a":
        produse_qs = produse_qs.order_by('pret')
    elif sort == "d":
        produse_qs = produse_qs.order_by('-pret')

    paginator = Paginator(produse_qs, items)
    nrPagina = request.GET.get("pagina")
    try:
        obPagina = paginator.page(nrPagina)
    except PageNotAnInteger:
        obPagina = paginator.page(1)
    except EmptyPage:
        obPagina = paginator.page(paginator.num_pages)
        mesajEroare = "Nu mai sunt produse"

    return render(request, 'aplicatie/produse.html', {
        'pagina': obPagina,
        'eroare': mesajEroare,
        'form': form
    })



def detalii_produs(request, id):
    try:
        produs = Articol.objects.get(id=id)
    except Articol.DoesNotExist:
        return render(request, 'aplicatie/eroare.html') 
    marimi = produs.marimi.all()
    return render(request, 'aplicatie/detalii_produs.html', {
        'produs': produs,
        'marimi': marimi
    })
    
def categorie(request, categorie_nume): 
    try:
        cat = Categorie.objects.get(nume=categorie_nume)
        produse = Articol.objects.filter(categorie=cat)
    except Categorie.DoesNotExist:
        return render(request, 'aplicatie/eroare.html')
    nrpagina = request.GET.get("pagina")
    paginator = Paginator(produse, 5)
    mesajEroare = None
    try:
        obPagina = paginator.page(nrpagina)
    except PageNotAnInteger:
        obPagina = paginator.page(1)
    except EmptyPage:
        obPagina = None
        mesajEroare = "Nu mai sunt produse"

    form = FilterFormArticole(initial={'categorie': cat.id})
    form.fields['categorie'].widget.attrs['readonly'] = True
    form.fields['categorie'].widget.attrs['hidden'] = True 

    return render(request, 'aplicatie/produse.html', {
        'pagina': obPagina,
        'eroare': mesajEroare,
        'categorie': cat,
        'form': form,
        'categorie_url_param': cat.id,
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nume = form.cleaned_data["nume"]
            prenume = form.cleaned_data["prenume"]
            cnp = form.cleaned_data["cnp"]
            data_nasterii = form.cleaned_data["data_nasterii"]
            email = form.cleaned_data["email"]
            email_confirmare = form.cleaned_data["email_confirmare"]
            tip_mesaj = form.cleaned_data["tip_mesaj"]
            subiect = form.cleaned_data["subiect"]
            minim_zile_astepatare = form.cleaned_data["minim_zile_asteptare"]
            mesaj = form.cleaned_data["mesaj"]
            
        
            return render(request, "aplicatie/contact.html", {
                "form": ContactForm(),
                "success": "Mesajul a fost trimis."
            })
        else:
            return render(request, "aplicatie/contact.html", {
                "form": form
            })
    else:
        form = ContactForm()

    return render(request, "aplicatie/contact.html", {"form": form})


def cos_virtual(request):
    return render(request, 'aplicatie/cos_virtual.html')

def in_lucru(request):
    return render(request, 'aplicatie/in_lucru.html')

"""from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

def inregistrare(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                request.session.set_expiry(0)
                messages.success(request, 'Cont creat și autentificat cu succes.')
                return redirect('profil')
            messages.error(request, 'Contul a fost creat dar autentificarea a eșuat. Te rog autentifică-te manual.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    if request.method == 'POST' and not form.is_valid():
        for field, errs in form.errors.items():
            for e in errs:
                messages.error(request, f"{field}: {e}")
    return render(request, 'aplicatie/inregistrare.html', {'form': form})


from django.core.mail import send_mail

def trimite_email():
    send_mail(
        subject='Ceausescu Ana-Carina 242',
        message='Ceausescu Ana-Carina 242',
        html_message='<h1>Salut</h1><p>Ce mai faci?</p>',
        from_email='test.tweb.node@gmail.com',
        recipient_list=['test.tweb.node@gmail.com'],
        fail_silently=False,
    )
    
def trimite_email(request):
    trimite_email()
    return HttpResponse("Email trimis cu succes!")

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if form.cleaned_data.get('ramane_logat'):
                    request.session.set_expiry(24*60*60)  # 1 zi
                else:
                    request.session.set_expiry(0)  
                return redirect('profil')
            else:
                form.add_error(None, 'Nume utilizator sau parolă invalide.')
    else:
        form = LoginForm()
    return render(request, 'aplicatie/login.html', {'form': form})
    
@login_required(login_url='login')
def profil(request):
    return render(request, 'aplicatie/profil.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('home')
    
"""
