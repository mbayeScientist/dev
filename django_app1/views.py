from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import Result
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

# def companies(request):
#     companies = Company.objects.all().values()
#     template=loader.get_template('index.html')
#     context={
#         'companies':companies
#     }   
#     return HttpResponse(template.render(context,request))

# def search_company(request):
#     search_term = request.GET.get('search_term', '')
#     companies = Company.objects.filter(sector__icontains=search_term)
#     return render(request, 'your_template.html', {'companies': companies})

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