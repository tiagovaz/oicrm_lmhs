from django.contrib import admin

from lmhs.models import Principal, Auteur

class PrincipalAdmin(admin.ModelAdmin):
#    list_display = ('cote_calcul', 'auteur', 'titre', 'date', 'source', 'type', 'projet')
#    search_fields = ['cote_calcul', 'auteur', 'titre', 'source', 'type', 'projet']
#    list_filter   = ['type', 'projet', 'auteur']
	pass

admin.site.register(Principal, PrincipalAdmin)
admin.site.register(Auteur)
