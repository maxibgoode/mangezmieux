#-*- coding: utf-8 -*-
from django import forms
from core.models import *

class SearchForm(forms.Form):
	"""Formulaire de recherche de recettes"""

	#champs du formulaire
	nom = forms.CharField(label='Nom de la recette', required=False)
	duree = forms.ChoiceField(label='Durée', choices=(), required=False)
	difficulte = forms.ChoiceField(label='Difficulté', choices=(), required=False)
	categorie = forms.ChoiceField(label='Catégorie', choices=(), required=False)

	def __init__(self, *args, **kwargs):
		"""Constructeur du formulaire, c'est là que l'on rempli les listes déroulantes"""
		#constucteur de l'objet parent
		super(SearchForm, self).__init__(*args, **kwargs)

		#remplissage des listes
		self.fields['duree'].choices = (('-1', '-'), ('30', '< 30 min'), ('60', '< 1 h'), ('90', '< 1 h 30'), ('91', '> 1 h 30'))
		self.fields['difficulte'].choices = (('-1', '-'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))
		self.fields['categorie'].choices = [('-1', '-')] + [(cat.pk, cat.nom) for cat in Categorie.objects.all()]		