# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals
import django

from django.db import models

#import datetime
#YEAR_CHOICES = []
#for r in range(1580, (datetime.datetime.now().year+1)):
#    YEAR_CHOICES.append((r,r))

class Auteur(models.Model):
    cote_auteur = models.CharField(blank=True, unique=True, max_length=20)
    nom_auteur = models.CharField(blank=True, unique=True, max_length=200)

    def __unicode__(self):
       return self.nom_auteur

    class Meta:
        db_table = 'auteurs'

class Principal(models.Model):
    id = models.AutoField(primary_key=True)
#    annee_1re_publication = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    annee_1re_publication = models.IntegerField(max_length=4, blank=True, null=True)
    notice_id = models.TextField(db_column='notice_ID', blank=True, null=True)  # Field name made lowercase.
    annee_enregistrement = models.IntegerField(max_length=4, blank=True, null=True)
    cote_calcul = models.TextField(blank=True, null=True, verbose_name="Cote")
    annee_production = models.IntegerField(max_length=4, blank=True, null=True)
    cote_calcul_url = models.TextField(blank=True, null=True)
    auteur = models.ManyToManyField('Auteur')
    auteur_old = models.CharField(blank=True, null=True, max_length=100)
    cote_per_calcul = models.TextField(blank=True)
    collection = models.CharField(blank=True, max_length=50)
    tousindex_calcul = models.TextField(db_column='tousIndex_calcul', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.TextField(blank=True)
    cote_annee = models.IntegerField(max_length=4)
    cote_auteur = models.CharField(max_length=50)
#    cote_auteur = models.ForeignKey('Auteur', related_name='cote')
    cote_numero = models.IntegerField(blank=True, null=True)
    hash = models.BigIntegerField(blank=True, null=True)
    cote_prefixe = models.CharField(max_length=20)
    protection_droit_auteur = models.BooleanField(db_column='Protection_droit_auteur', blank=True, default=False)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    cal_support_enligne = models.TextField(db_column='Cal_support_EnLigne', blank=True)  # Field name made lowercase.
    depouillement = models.TextField(blank=True)
    directeur_collection = models.CharField(blank=True, max_length=20)
    directeur_publication = models.CharField(blank=True, max_length=20)
    editeur = models.CharField(blank=True, max_length=20)
    en_collection = models.CharField(blank=True, max_length=200)
    fonds = models.CharField(blank=True, max_length=50)
    genre = models.TextField(blank=True)
    id_org = models.TextField(blank=True)
    instrumentation = models.TextField(blank=True)
    interprete = models.TextField(blank=True)
    langue_origine = models.CharField(blank=True, max_length=20)
    lieu = models.CharField(blank=True, max_length=50)
    lieu_conservation = models.TextField(blank=True)
    localisation = models.CharField(blank=True, max_length=200)
    maison_edition = models.CharField(blank=True, max_length=50)
    medium = models.TextField(blank=True)
    methode_reproduction = models.TextField(blank=True)
    mot_cle = models.CharField(blank=True, max_length=50)
    nb_exemplaire = models.IntegerField(blank=True, null=True)
    nb_page = models.CharField(blank=True, max_length=20)
    nb_volume = models.CharField(blank=True, max_length=20)
    no_page = models.CharField(blank=True, max_length=20)
    no_volume = models.CharField(blank=True, max_length=20)
    nom_org = models.TextField(blank=True)
    organisme = models.TextField(blank=True, null=True)
    projet = models.CharField(blank=True, null=True, max_length=200)
    source = models.CharField(blank=True, max_length=200)
    source_per = models.CharField(blank=True, max_length=200)
    source_per_calcul = models.TextField(blank=True, null=True)
    sujet = models.TextField(blank=True)
    support = models.CharField(blank=True, max_length=200)
    titre = models.CharField(blank=True, max_length=50)
    traducteur = models.CharField(blank=True, max_length=50)
    type = models.TextField()
    type_evenement = models.TextField(blank=True)
    cal_support_list_moins_enligne = models.TextField(db_column='Cal_support_List_moins_EnLigne', blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'LMHS_principale'

