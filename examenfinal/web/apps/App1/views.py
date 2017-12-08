

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class vistaPrincipal(TemplateView):
	template_name = 'index.html'

 		

