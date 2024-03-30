from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import User
import subprocess
from django.contrib.staticfiles import finders

def index(request):
    user=User.objects.all()
    template=loader.get_template('index.html')
    context={
        'user':user,
    }   
    return HttpResponse(template.render(context,request))



from .models import Company



def companies(request):
    search_term = request.GET.get('search_term', '')  # Obtenez le terme de recherche de la requête GET
    if search_term:
        # Filtrer les entreprises par secteur en utilisant le terme de recherche
        companies = Company.objects.filter(sector__icontains=search_term)
    else:
        # Aucun terme de recherche spécifié, renvoyer toutes les entreprises
        companies = Company.objects.all()

    context = {
        'companies': companies
    }
    return render(request, 'index.html', context)


from django.db.models import Q
from .models import Chaussure

from django.shortcuts import render
from django.db.models import Q
from .models import Chaussure

def chaussure_search(request):
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    sexe = request.GET.get('sexe', '').lower()
    produits_moins_chers = Chaussure.objects.all().order_by('price_cfa').distinct()[:4]
    produits_plus_chers = Chaussure.objects.all().order_by('-price_cfa').distinct()[:4]
    #prenons les 4 premieres chaussures en evitant les doublons

    # Commencez par filtrer en fonction des prix
    price_query = Q()
    if price_min:
        try:
            price_min = float(price_min)
            price_query &= Q(price_cfa__gte=price_min)
        except ValueError:
            pass  # Ignorez le filtre si la conversion échoue

    if price_max:
        try:
            price_max = float(price_max)
            price_query &= Q(price_cfa__lte=price_max)
        except ValueError:
            pass  # Ignorez le filtre si la conversion échoue

    chaussures = Chaussure.objects.filter(price_query)

    # Appliquez ensuite le filtre sur le sexe sur le résultat filtré par prix
    if sexe:
        sexe_query = Q()
        if sexe == 'f':
            sexe_query &= Q(title__icontains='femme')
        elif sexe == 'm':
            sexe_query &= Q(title__icontains='homme')
        
        chaussures = chaussures.filter(sexe_query)
        
    context = {
        'chaussures': chaussures,
        'price_min': price_min,
        'price_max': price_max,
        'sexe': sexe,
        'produits_moins_chers': produits_moins_chers,
        'produits_plus_chers': produits_plus_chers
    }

    return render(request, 'index1.html', context)


