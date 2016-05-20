#!/usr/bin/python
 # -*- coding: utf-8 -*-

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab, FormActions, StrictButton
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, Div
from models import *


class Search(forms.ModelForm, Layout):
    auteur = forms.CharField(label="Auteur")
    titre = forms.CharField(label="Titre du document")
    titre_periodique = forms.CharField(label="Titre du périodique")
    recherche_pdf = forms.CharField(label="Recherche plein text")
    mot_cles = forms.CharField(label="Mot-clé")
    projet_list = [ "", "Anthologie d'articles de presse sur Albéric Magnard", "Ballets français (1917-1939)", "Enquêtes et entrevues avec des musiciens", "Esthétique musicale en France (1900-1950)", "Modern Music", "Musiques anciennes", "Musique d’avant-garde dans les périodiques français (1880-1902)", "Nouveaux médias et jazz", "Programmes de la Société musicale indépendante", "Sociologie de la musique au Québec" ]
    type_list = [ "", "Affiche", "Annonce de concours", "Article de périodique", "Catalogue", "Conférence", "Document non publié", "Extrait de livre", "Iconographie", "Livre", "Matériel audiovisuel", "Partition", "Périodique", "Photographie", "Programme", "Référence" ]
    tousIndex_calcul = forms.CharField(label="Tous les index")
    projet = forms.ChoiceField(choices=sorted(set([(i, i) for i in projet_list])))
    type = forms.ChoiceField(choices=sorted(set([(i, i) for i in type_list])))
    helper = FormHelper()
    helper.form_method = 'GET'
    helper.form_action = '/result/'
    helper.add_input(Submit('submit', 'Chercher'))

    helper.layout = Layout (
            Div(
                    Div( 'auteur', css_class='col-sm-6'),
                    Div( 'recherche_pdf', css_class='col-sm-6'),
                    css_class='row'
            ),
            Div(

                    Div( 'titre', css_class='col-sm-6'),
                    Div( 'tousIndex_calcul', css_class='col-sm-6'),
                    css_class='row'
            ),
            Div(
                    Div( 'date', css_class='col-sm-6'),
                    Div( 'projet', css_class='col-sm-6'),
                    css_class='row'
            ),
            Div(
                    Div( 'titre_periodique', css_class='col-sm-6'),
                    Div( 'type', css_class='col-sm-6'),
                    css_class='row'
            ),
            Div(
                    Div( 'mot_cles', css_class='col-sm-6'),
                    css_class='row'
            ),
    )

    class Meta:
        model = Principal
        fields = '__all__'

#######################################################################

class CommonLayoutLivre(forms.ModelForm, Layout):
    def __init__(self, *args, **kwargs):
        super(CommonLayoutLivre, self).__init__(*args, **kwargs)


        self.fields['cote_auteur'] = forms.ChoiceField(choices=set([(f.cote_auteur, f.cote_auteur) for f in Auteur.objects.all()]))
        #self.fields['cote_prefixe'] = forms.ChoiceField(choices=set([(f.cote_prefixe, f.cote_prefixe) for f in Principal.objects.all()]))
        prefixe_list = [ "A", "ART", "CAT", "CONC", "CONF", "DNP", "EXT", "ICO", "L", "MA", "MUS", "PER", "PROG", "REF" ]
        type_list = [ "Affiche", "Annonce de concours", "Article de périodique", "Catalogue", "Conférence", "Document non publié", "Extrait de livre", "Iconographie", "Livre", "Matériel audiovisuel", "Partition", "Périodique", "Photographie", "Programme", "Référence" ]
        type_evenement_liste = [ "", "Concert | calendrier mensuel", "Concert | concert unique", "Concert | festival", "Concert | plusieurs représentations", "Concert | saison", "Concert | série de concerts", "Colloque", "Conférence", "Divers", "Émission radiophonique", "Événement mixte", "Exposition", "Interview", "Journée d'étude" ]
        support_list = [ "", "En ligne", "Cassette", "CD", "CD-Rom", "DVD", "DVD-Rom", "Papier" ]
        projet_list = [ "", "Anthologie d'articles de presse sur Albéric Magnard", "Ballets français (1917-1939)", "Enquêtes et entrevues avec des musiciens", "Esthétique musicale en France (1900-1950)", "Modern Music", "Musiques anciennes", "Musique d’avant-garde dans les périodiques français (1880-1902)", "Nouveaux médias et jazz", "Programmes de la Société musicale indépendante", "Sociologie de la musique au Québec" ]

        self.fields['cote_prefixe'] = forms.ChoiceField(choices=set([(i, i) for i in prefixe_list]))
        self.fields['support'] = forms.ChoiceField(choices=sorted(set([(i, i) for i in support_list])), required=False)
        self.fields['projet'] = forms.ChoiceField(choices=sorted(set([(i, i) for i in projet_list])), required=False)

        self.fields['type'].label = False
        self.fields['cote_prefixe'].label = "Cote (prefixe)"
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
        self.fields['mot_cle'].label = "Mot-clé"
        self.fields['traducteur'].label = "Traducteur(s)"
        self.fields['langue_origine'].label = "Langue d'origine"


        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = '/submit_data/'
        self.helper.add_input(Submit('submit', 'Enregistrer'))


        self.helper.layout = Layout (
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
        )

    class Meta:
        model = Principal
        fields = '__all__'

class Livre(CommonLayoutLivre):

    def __init__(self, *args, **kwargs):
        super(Livre, self).__init__(*args, **kwargs)

        self.helper.layout.extend(
            Layout(
                Field('type', type='hidden', value='Livre'),

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
        )

class ExtraitLivre(CommonLayoutLivre):

    def __init__(self, *args, **kwargs):
        super(ExtraitLivre, self).__init__(*args, **kwargs)

        self.helper.layout.extend(
            Layout(
                Field('type', type='hidden', value='Extrait de livre'),

                Div(
                        Div( 'editeur', css_class='col-sm-4'),
                        Div( 'lieu', css_class='col-sm-4' ),
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
                        Div( 'source', css_class='col-sm-4'),
                        Div( 'nb_page', css_class='col-sm-4' ),
                        Div( 'nb_exemplaire', css_class='col-sm-4' ),
                        css_class='row'
                ),
                Div(
                        Div( 'fonds', css_class='col-sm-12'),
                        css_class='row'
                ),
                Div(
                        Div( 'commentaire', css_class='col-sm-12'),
                        css_class='row'
                ),
            )

        )


class Periodique(CommonLayoutLivre):

    def __init__(self, *args, **kwargs):
        super(Periodique, self).__init__(*args, **kwargs)

        self.helper.layout.extend(
            Layout(
                Field('type', type='hidden', value='Périodique'),
                Div(
                        Div( 'en_collection', css_class='col-sm-6'),
                        Div( 'mot_cle', css_class='col-sm-6'),
                        css_class='row'
                ),
                Div(
                        Div( 'fonds', css_class='col-sm-12'),
                        css_class='row'
                ),
                Div(
                        Div( 'commentaire', css_class='col-sm-12'),
                        css_class='row'
                ),
            )
        )

class ArticlePeriodique(CommonLayoutLivre):

    def __init__(self, *args, **kwargs):
        super(ArticlePeriodique, self).__init__(*args, **kwargs)

        self.helper.layout.extend(
            Layout(
                Field('type', type='hidden', value='Article de périodique'),

                Div(
                        Div( 'date', css_class='col-sm-4'),
                        Div( 'source_per', css_class='col-sm-4'),
                        Div( 'mot_cle', css_class='col-sm-4'),
                        css_class='row'
                ),
                Div(
                        Div( 'no_page', css_class='col-sm-4' ),
                        Div( 'nb_exemplaire', css_class='col-sm-4' ),
                        Div( 'support', css_class='col-sm-4'),
                        css_class='row'
                ),
                Div(
                        Div( 'projet', css_class='col-sm-6'),
                        Div( 'localisation', css_class='col-sm-6'),
                        css_class='row'
                ),
                Div(
                        Div( 'fonds', css_class='col-sm-12'),
                        css_class='row'
                ),
                Div(
                        Div( 'commentaire', css_class='col-sm-12'),
                        css_class='row'
                ),
            )

        )

