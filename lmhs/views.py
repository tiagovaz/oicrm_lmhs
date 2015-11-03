from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response
from django.views.generic import View
from forms import *

import re

from django.db.models import Q

class SimpleSearchForm(View):
    def get(self, request):
        simple_search_form = SimpleSearch()
        return render(request, 'simple_search.html', {'form': simple_search_form})

    def post(self, request):
        pass

class Gallery(View):
    def get(self, request):
        return render(request, 'gallery.html')

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
