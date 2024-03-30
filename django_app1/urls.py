from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('chaussure/', views.chaussure_search,name='chaussure-search'),
    path('', views.companies, name='companies'),
]

