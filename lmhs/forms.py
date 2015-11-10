#!/usr/bin/python
 # -*- coding: utf-8 -*-

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab, FormActions, StrictButton
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, Div
from models import *


class CommonLayout(forms.ModelForm, Layout):
    code = forms.CharField(
        label='Serial Number',
        max_length=12,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(CommonLayout, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'

        self.helper.layout = Layout (
            #Field('code', css_class='form-control', placeholder='Read the Serial Number'),
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
        )

    class Meta:
        model = Principal
        fields = '__all__'

#the class with the form
class Livre(CommonLayout):

    def __init__(self, *args, **kwargs):
        super(Livre, self).__init__(*args, **kwargs)

        self.helper.form_action = 'collection'

        self.helper.layout.extend(
            Layout(
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


        self.helper.layout.append(
            FormActions(
                StrictButton('Pass', type="submit", name="result", value="True", css_class="btn btn-success"),
            )
        )
