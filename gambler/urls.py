from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView, TemplateView

from gambler.models import Apuesta
from gambler.forms import ApuestaForm
from django.conf.urls import patterns, url
from gambler.views import *
from gambler.views import ApuestaCreate, PartidoDetail, PartidoList, EquipoList, ApuestaList, ResultadoList

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
        url(r'^partidos\.(?P<extension>(json|xml))$',
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

    # Partido apuesta details, ex: /gambler/gambler/1/apuestaes/1/
    url(r'^partido/(?P<pkr>\d+)/apuesta/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Apuesta,
            template_name='gambler/apuestas_detail.html'),
        name='apuesta_detail'),

    # Create a partido apuesta, ex: /gambler/partido/1/apuesta/create/
    url(r'^partido/(?P<pk>\d+)/apuesta/create/$',
        ApuestaCreate.as_view(),
        name='apuesta_create'),

    # Edit partido apuesta details, ex: /gambler/partido/1/apuesta/1/edit/
    url(r'^partido/(?P<pkr>\d+)/apuesta/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Apuesta,
            form_class=ApuestaForm,
            template_name='gambler/form.html'),
        name='apuesta_edit'),

)
