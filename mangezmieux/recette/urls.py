from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^recherche/$', 'recette.views.recherche'),
	url(r'^categorie/$', 'recette.views.categorie'),
	url(r'^categorie/(?P<id>\d*)/$', 'recette.views.categorie'),
	url(r'^detail/(?P<id>\d*)/$', 'recette.views.detail'),
        url(r'^suggestion/$', 'recette.views.suggestion'),
    url(r'^favoriser/(?P<id>\d*)/?$', 'recette.views.ajout_favoris'),
    url(r'^defavoriser/(?P<id>\d*)/?$', 'recette.views.retrait_favoris'),
    url(r'^ajouter/?$', 'recette.views.ajouter_recette'),
    url(r'^mesrecettes/$', 'recette.views.mes_recettes'),
    url(r'^get-produit/?$', 'recette.views.get_produit'),
)
