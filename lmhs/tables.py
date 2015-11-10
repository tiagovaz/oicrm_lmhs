import django_tables2 as tables
from models import Principal
from django_tables2.utils import A  # alias for Accessor

class PrincipalTable(tables.Table):
    # using auteur_old to list old system records while it's not migrated to a proper m2m...
#    auteur = tables.Column(accessor='auteur', verbose_name='Auteurs')
    date = tables.Column(verbose_name='Date')
    titre = tables.Column(accessor='titre', verbose_name='Titre')
    auteur = tables.Column(accessor='auteur_old', verbose_name='Auteur(es)')
    edit = tables.LinkColumn('item_edit', args=[A('pk')], orderable=False, empty_values=())

    def render_edit(self):
        return 'Edit'

#    def render_auteur(self, record):
#        if record.auteur.exists():
#            l = [p.nom_auteur for p in record.auteur.all()]
#            return ', '.join(l)
#

    class Meta:
        model = Principal
        #debug:
        #fields = ('id', 'cote_prefixe', 'cote_auteur', 'cote_numero', 'cote_annee', 'titre', 'date')
        fields = ('titre', 'date')
        attrs = {"class": "paleblue"}
