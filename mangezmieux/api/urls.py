#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from views import *

"""
URLs relativent aux différents points de l'API.
Les URLs sont généralement regroupées par modèles. 
"""

urlpatterns = patterns('',

	url(r'^$', 'core.api.api_root'),

	url(r'^obtenirToken/$', 'rest_framework.authtoken.views.obtain_auth_token'),
    
#    url(r'^repas/ajouter-repas/$', 'core.api.ajouter_repas'),
    url(r'^repas/retirerRecette/(?P<pk>\d+)/$', RepasRetirer.as_view(), name='repas-retirer'),
    url(r'^planning/generer/$', PlanningGenerer.as_view(), name='planning-generer'),
    
    url(r'^unites/$', UniteList.as_view(), name='unite-list'),
    url(r'^unites/(?P<pk>\d+)/$', UniteDetail.as_view(), name='unite-detail'),
    
    url(r'^typeProduits/$', TypeProduitList.as_view(), name='typeproduit-list'),
    url(r'^typeProduits/(?P<pk>\d+)/$', TypeProduitDetail.as_view(), name='typeproduit-detail'),
    
    url(r'^ligneRecettes/$', LigneRecetteList.as_view(), name='lignerecette-list'),
    url(r'^ligneRecettes/(?P<pk>\d+)/$', LigneRecetteDetail.as_view(), name='lignerecette-detail'),
    
    url(r'^ligneProduits/$', LigneProduitList.as_view(), name='ligneproduit-list'),
    url(r'^ligneProduits/(?P<pk>\d+)/$', LigneProduitDetail.as_view(), name='ligneproduit-detail'),
    
    url(r'^categories/$', CategorieList.as_view(), name='categorie-list'),
    url(r'^categories/(?P<pk>\d+)/$', CategorieDetail.as_view(), name='categorie-detail'),
    
    url(r'^commandes/$', CommandeList.as_view(), name='commande-list'),
    url(r'^commandes/(?P<pk>\d+)/$', CommandeDetail.as_view(), name='commande-detail'),
    url(r'^commandes/commander/$', CommandeCommander.as_view(), name='commande-commander'),
    
    url(r'^ligneCommandes/$', LigneCommandeList.as_view(), name='lignecommande-list'),
    url(r'^ligneCommandes/(?P<pk>\d+)/$', LigneCommandeDetail.as_view(), name='lignecommande-detail'),
    
    url(r'^utilisateurs/$', UserList.as_view(), name='user-list'),
    url(r'^utilisateurs/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    
    url(r'^repas/$', RepasList.as_view(), name='repas-list'),
    url(r'^repas/(?P<pk>\d+)/$', RepasDetail.as_view(), name='repas-detail'),
    
    url(r'^recettes/$', RecetteList.as_view(), name='recette-list'),
    url(r'^recettes/suggestion/$', RecetteSuggestion.as_view(), name='recette-suggestion'),
    url(r'^recettes/(?P<pk>\d+)/$', RecetteDetail.as_view(), name='recette-detail'),
    url(r'^recettes/mesrecettes/$', RecettePersonnelles.as_view(), name='recette-personnelles'),
   
    url(r'^recettesFavorites/$', RecetteFavoriteList.as_view(), name='recettefavorite-list'),
    url(r'^recettesFavorites/supprimer/(?P<pk>[0-9]+)/$', RecetteFavoriteSuppression.as_view(), name='recettefavorite-suppression'),
    
    url(r'^produits/$', ProduitList.as_view(), name='produit-list'),
    url(r'^produits/(?P<pk>\d+)/$', ProduitDetail.as_view(), name='produit-detail'),

    url(r'^news/$', NewsList.as_view(), name='news-list'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news-detail'),
    
    url(r'^lignePaniers/$', LignePanierList.as_view(), name='lignepanier-list'),
    url(r'^lignePaniers/(?P<pk>\d+)/$', LignePanierDetail.as_view(), name='lignepanier-detail'),
    url(r'^lignePaniers/supprimer/(?P<pk>[0-9]+)/$', LignePanierSuppression.as_view(), name='lignepanier-suppression'),
    
    url(r'^paniers/$', PanierDetail.as_view(), name='panier-detail'),
    url(r'^paniers/generer/$', PanierGenerer.as_view(), name='panier-generer'),
    url(r'^paniers/supprimer/(?P<pk>[0-9]+)/$', PanierSuppression.as_view(), name='panier-suppression'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


