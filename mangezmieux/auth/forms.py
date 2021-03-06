#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.forms.widgets import HiddenInput
from django import forms
from models import ProfilUtilisateur

class FormulaireInscription(forms.Form):
	"""
	Formulaire d'inscription avec : 
		username,
		nom, 
		prénom, 
		email unique, 
		mot de passe avec confirmation

	"""
	username = forms.RegexField(regex=r'^[\w.@+-]+$',max_length=30,widget=forms.TextInput(),label="Nom d'utilisateur",error_messages={'Invalide': "L'identifiant ne peut contenir que des caractères alphanumériques, \"@\",\".\",\"+\",\"-\" et\"_\"."})
	nom = forms.CharField(widget=forms.TextInput(), label="Nom")
	prenom = forms.CharField(widget=forms.TextInput(), label="Prénom")
	email = forms.EmailField(widget=forms.TextInput(),label="E-mail")
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),label="Mot de passe")
	password_confirm = forms.CharField(widget=forms.PasswordInput(render_value=False),label="Confirmation du mot de passe")


	def clean(self):
		"""
			Fonction vérifiant que les deux mots de passe sont bien identiques
		"""
		if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
				self._errors['password'] = [u'Les mots de passe doivent être identiques.']
				self._errors['password_confirm'] = [u'Les mots de passe doivent être identiques.']
		return self.cleaned_data

	def clean_email(self):
		"""
			Fonction vérifiant que l'adresse email n'est pas déjà utilisée
		"""
		if User.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError("Cette adresse email est déjà associée à un compte.")
		return self.cleaned_data['email']

	def clean_username(self):
		"""
			Fonction vérifiant que l'adresse email n'est pas déjà utilisée
		"""
		if User.objects.filter(username__iexact=self.cleaned_data['username']):
			raise forms.ValidationError("Ce username est déjà associée à un compte.")
		return self.cleaned_data['username']


class FormulaireUtilisateur(UserChangeForm):
	"""
	Formulaire permettant de modifier les données d'un utilisateur
	"""
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password')

	def __init__(self, *args, **kwargs):
		super(UserChangeForm, self).__init__(*args, **kwargs)
		self.fields['password'].widget = HiddenInput()

class FormulaireProfil(forms.ModelForm):
	"""
	Formulaire d'édition du profil utilisateur
	"""
	class Meta:
		model = ProfilUtilisateur
		fields = ('nbPersonnes', 'gouts')

	def __init__(self, *args, **kwargs):
		super(forms.ModelForm, self).__init__(*args, **kwargs)
		self.fields['nbPersonnes'].label = "Nombre de personnes pour les repas"

