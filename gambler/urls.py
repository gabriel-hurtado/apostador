from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView, TemplateView

from gambler.models import Apuesta
from gambler.forms import ApuestaForm
from django.conf.urls import patterns, url
from gambler.views import *

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),



    # List latest 5 partido: /gambler/partidos
    url(r'^partidos$', PartidoList.as_view(), name='partidos_list'),

     # List latest 5 equipo: /gambler/equipos
    url(r'^equipos$', EquipoList.as_view(), name='equipos_list'),

    # List gambler: /gambler/partidos.json
        url(r'^partidos\.(?P<extension>(json|xml))$',
        PartidoList.as_view(),
        name='partido_list_conneg'),

    # List equipos: /gambler/equipos.json
    url(r'^equipos\.(?P<extension>(json|xml))$',
        EquipoList.as_view(),
        name='equipo_list_conneg'),

    # Partido details, ex.: /gambler/gambler/1/
    url(r'^gambler/(?P<pk>\d+)/$',
        PartidoDetail.as_view(),
        name='partido_detail'),

    # Equipo details, ex.: /gambler/gambler/1/
    url(r'^gambler/(?P<pk>\d+)/$',
        EquipoDetail.as_view(),
        name='equipo_detail'),

    # Partido details, ex.: /gambler/gambler/1.json
    url(r'^gambler/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        PartidoDetail.as_view(),
        name='partido_detail_conneg'),

    # Equipo details, ex.: /gambler/gambler/1.json
    url(r'^gambler/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        EquipoDetail.as_view(),
        name='equipo_detail_conneg'),

    # Partido apuesta details, ex: /gambler/gambler/1/apuestaes/1/
    url(r'^gambler/(?P<pkr>\d+)/apuestaes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Apuesta,
            template_name='gambler/apuesta_detail.html'),
        name='apuesta_detail'),

    # Create a partido apuesta, ex: /gambler/gambler/1/apuestaes/create/
    url(r'^gambler/(?P<pk>\d+)/apuestaes/create/$',
        ApuestaCreate.as_view(),
        name='apuesta_create'),

    # Edit partido apuesta details, ex: /gambler/gambler/1/apuestaes/1/edit/
    url(r'^gambler/(?P<pkr>\d+)/apuestaes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Apuesta,
            form_class=ApuestaForm,
            template_name='gambler/form.html'),
        name='apuesta_edit'),

)
