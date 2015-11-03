import django_tables2 as tables
from models import Principal

class PrincipalTable(tables.Table):
    class Meta:
        model = Principal
        attrs = {"class": "paleblue"}
