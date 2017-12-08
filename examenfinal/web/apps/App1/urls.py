

from django.conf.urls import url,include
from .views import vistaPrincipal

urlpatterns = [

    url(r'^$', vistaPrincipal.as_view()),	
	url(r'^principal$', vistaPrincipal.as_view(), name = 'principal'),
]
