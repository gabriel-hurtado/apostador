from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView, TemplateView

from gambler.models import Apuesta
from gambler.forms import ApuestaForm
from django.conf.urls import patterns, url
from gambler.views import *
from gambler.views import ApuestaCreate, PartidoDetail, ApuestaDetail, PartidoList, EquipoList, ApuestaList, ResultadoList

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),


    # List latest 5 apuesta: /gambler/apuestas
    url(r'^apuestas$', ApuestaList.as_view(), name='apuestas_list'),

    # List latest 5 partido: /gambler/partidos
    url(r'^partidos$', PartidoList.as_view(), name='partidos_list'),

     # List latest 5 equipo: /gambler/equipos
    url(r'^equipos$', EquipoList.as_view(), name='equipos_list'),

     # List latest 5 equipo: /gambler/equipos
    url(r'^resultados$', ResultadoList.as_view(), name='resultados_list'),

    # List partidos: /gambler/partidos.json
        url(r'^partidos\.(?P<extension>(json| xml))$',
        PartidoList.as_view(),
        name='partido_list_conneg'),

    # List equipos: /gambler/equipos.json
    url(r'^equipos\.(?P<extension>(json|xml))$',
        EquipoList.as_view(),
        name='equipo_list_conneg'),

    # List apuestas: /gambler/apuestas.json
    url(r'^apuestas\.(?P<extension>(json|xml))$',
        ApuestaList.as_view(),
        name='apuesta_list_conneg'),

    # List resultados: /gambler/resultados.json
    url(r'^resultados\.(?P<extension>(json|xml))$',
        ResultadoList.as_view(),
        name='resultado_list_conneg'),

    # Partido details, ex.: /gambler/partido/1/
    url(r'^partido/(?P<pk>\d+)/$',
        PartidoDetail.as_view(),
        name='partido_detail'),

    # Partido details, ex.: /gambler/partido/1.json
    url(r'^partido/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        PartidoDetail.as_view(),
        name='partido_detail_conneg'),

    # Apuesta details, ex.: /gambler/partido/1/
    url(r'^apuesta/(?P<pk>\d+)/$',
        ApuestaDetail.as_view(),
        name='apuesta_detail'),

    # Apuesta details, ex.: /gambler/apuesta/1.json
    url(r'^apuesta/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        ApuestaDetail.as_view(),
        name='apuesta_detail_conneg'),

    # Create a partido apuesta, ex: /gambler/partido/1/apuesta/create/
    url(r'^partido/(?P<pk>\d+)/apuesta/create/$',
        ApuestaCreate.as_view(),
        name='apuesta_create'),
)
