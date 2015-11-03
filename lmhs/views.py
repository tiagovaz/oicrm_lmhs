from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response
from django.views.generic import View
from django_tables2   import RequestConfig
from models import Principal
from tables import PrincipalTable

from forms import *

import re

from django.db.models import Q

class SearchForm(View):
    def get(self, request):
        search_form = Search()
        return render(request, 'search.html', {'form': search_form})

    def post(self, request):
        pass

class Result(View):
    def get(self, request):
        pass

    def post(self, request):
        return render(request, 'result.html')

class AllData(View):
    def get(self, request):
        data = Principal.objects.all()
        data_table = PrincipalTable(data)
        data_table.paginate(page=request.GET.get('page', 1), per_page=25)
        return render_to_response('all.html', {'table': data_table}, context_instance=RequestContext(request))

    def post(self, request):
        pass

class NewForm(View):
    def get(self, request):
	# form class name is the same in url/?form=VALUE
	new_form = eval(request.GET.get('f'))
	label = request.GET.get('l')
        return render(request, 'new.html', {'form': new_form, 'label': label})

    def post(self, request):
        pass


class InsertPrincipal(View):
    def get(self, request):
	return HttpResponseRedirect('/new/?f=Livre&l=Livre')

    def post(self, request):
#	new_form = eval(request.POST.get('formClass'))
	livreForm = Livre(request.POST)
        if livreForm.is_valid():
            print livreForm
            livreForm.save()
            return HttpResponseRedirect('/new/?f=Livre&l=Livre')
        else:
            messages.error(request, "Error")

        return render_to_response("new.html", {"form": livreForm}, context_instance=RequestContext(request))

class InsertAuteur(View):
    def get(self, request):
	pass

    def post(self, request):
        pass
