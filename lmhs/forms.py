#!/usr/bin/python
 # -*- coding: utf-8 -*-

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, Div
from models import *

class SimpleSearch(forms.ModelForm):
    class Meta:
        model = Principal
        fields = '__all__'

class FormBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormBase, self).__init__(*args, **kwargs)
        self.fields['cote_auteur'] = forms.ChoiceField(choices=set([(f.cote_auteur, f.cote_auteur) for f in Auteur.objects.all()]))
        self.fields['cote_prefixe'] = forms.ChoiceField(choices=set([(f.cote_prefixe, f.cote_prefixe) for f in Principal.objects.all()]))
        self.fields['type'].label = False
        self.fields['cote_prefixe'].label = "Cote (prefix)"
        self.fields['cote_auteur'].label = "(auteur)"
        self.fields['cote_annee'].label = "(année)"
        self.fields['cote_numero'].label = "(numéro)"
        self.fields['editeur'].label = "Éditeur(s)"
        self.fields['titre'].label = "Titre"
        self.fields['auteur'].label = "Auteur(s)"
        self.fields['lieu'].label = "Lieu"
        self.fields['maison_edition'].label = "Maison d'édition"
        self.fields['protection_droit_auteur'].label = "Public"
        self.fields['directeur_publication'].label = "Directeur(s) de la publication"
        self.fields['directeur_collection'].label = "Directeur(s) de la collection"
        self.fields['annee_1re_publication'].label = "Année de 1re publication"
        self.fields['nb_volume'].label = "Nombre de volume"
        self.fields['nb_page'].label = "Nombre de page"
        self.fields['nb_exemplaire'].label = "Nombre d'exemplaire"
        self.fields['date'].label = "Date"
        self.fields['mot_cle'].label = "Mot(s) clé(s)"
        self.fields['traducteur'].label = "Traducteur(s)"
        self.fields['langue_origine'].label = "Langue d'origine"

class Livre(FormBase):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = '/submit_data/'
    helper.add_input(Submit('submit', 'Enregistrer'))

    helper.layout = Layout(
		# used to commit the obj save
		Field('formClass', type='hidden', value='Livre'),
		Field('type', type='hidden', value='livre'),
		Div(
			Div( 'cote_prefixe', css_class='col-sm-2' ),
			Div( 'cote_auteur', css_class='col-sm-2'),
			Div( 'cote_annee', css_class='col-sm-2'),
			Div( 'cote_numero', css_class='col-sm-2'),
			Div( 'protection_droit_auteur', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'titre', css_class='col-sm-12'),
			css_class='row'
		),
		Div(
			Div( Field('auteur', css_class='chosen'), css_class='col-sm-12'),
			css_class='row'
		),
		Div(
			Div( 'editeur', css_class='col-sm-4'),
			Div( 'lieu', css_class='col-sm-4' ),
			Div( 'maison_edition', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'annee_1re_publication', css_class='col-sm-4' ),
			Div( 'directeur_publication', css_class='col-sm-4'),
			Div( 'date', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'langue_origine', css_class='col-sm-4' ),
			Div( 'traducteur', css_class='col-sm-4'),
			Div( 'mot_cle', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'nb_page', css_class='col-sm-4' ),
			Div( 'nb_exemplaire', css_class='col-sm-4' ),
			Div( 'nb_volume', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'collection', css_class='col-sm-4' ),
			Div( 'directeur_collection', css_class='col-sm-4'),
			Div( 'fonds', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'commentaire', css_class='col-sm-12'),
			css_class='row'
		),
    )


    class Meta:
        model = Principal
	fields = '__all__'

class ExtraiteLivre(FormBase):
    #cote_auteur = forms.ModelChoiceField(queryset=Auteur.objects.values_list('cote_auteur', flat=True).distinct())
    cote_prefixe = forms.ModelChoiceField(Principal.objects.values_list('cote_prefixe', flat=True).distinct())

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = 'submit_data'
    helper.add_input(Submit('submit', 'Enregistrer'))

    helper.layout = Layout(
		Field('type', type='hidden', value='livre'),
		Div(
			Div( 'cote_prefixe', css_class='col-sm-2' ),
			Div( 'cote_auteur', css_class='col-sm-2'),
			Div( 'cote_annee', css_class='col-sm-2'),
			Div( 'cote_numero', css_class='col-sm-2'),
			Div( 'protection_droit_auteur', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'titre', css_class='col-sm-12'),
			css_class='row'
		),
		Div(
			Div( Field('auteur', css_class='chosen'), css_class='col-sm-12'),
			css_class='row'
		),
		Div(
			Div( 'editeur', css_class='col-sm-4'),
			Div( 'lieu', css_class='col-sm-4' ),
			Div( 'maison_edition', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'annee_1re_publication', css_class='col-sm-4' ),
			Div( 'directeur_publication', css_class='col-sm-4'),
			Div( 'date', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'langue_origine', css_class='col-sm-4' ),
			Div( 'traducteur', css_class='col-sm-4'),
			Div( 'mot_cle', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'nb_page', css_class='col-sm-4' ),
			Div( 'nb_exemplaire', css_class='col-sm-4' ),
			Div( 'nb_volume', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'collection', css_class='col-sm-4' ),
			Div( 'directeur_collection', css_class='col-sm-4'),
			Div( 'fonds', css_class='col-sm-4'),
			css_class='row'
		),
		Div(
			Div( 'commentaire', css_class='col-sm-12'),
			css_class='row'
		),
    )


    class Meta:
        model = Principal
	fields = '__all__'

class Search(FormBase):
    def __init__(self, *args, **kwargs):
        super(FormBase, self).__init__(*args, **kwargs)

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = '/result/'
    helper.add_input(Submit('submit', 'Enregistrer'))

    helper.layout = Layout(
                Div(
                        Div( 'titre', css_class='col-sm-12'),
                        css_class='row'
                ),
                Div(
                        Div( Field('auteur', css_class='chosen'), css_class='col-sm-12'),
                        css_class='row'
                ),
    )

    class Meta:
        model = Principal
        fields = '__all__'

