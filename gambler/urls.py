from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView

from gambler.models import Partido, Apuesta
from gambler.forms import PartidoForm, ApuestaForm
from gambler.views import PartidoCreate, ApuestaCreate, PartidoDetail, PartidoList

urlpatterns = patterns('',
    # List latest 5 gambler: /gambler/
    url(r'^$',
        PartidoList.as_view(),
        name='partido_list'),
    # List gambler: /gambler/gambler.json
    url(r'^gambler\.(?P<extension>(json|xml))$',
        PartidoList.as_view(),
        name='partido_list_conneg'),

    # Partido details, ex.: /gambler/gambler/1/
    url(r'^gambler/(?P<pk>\d+)/$',
        PartidoDetail.as_view(),
        name='partido_detail'),
    # Partido details, ex.: /gambler/gambler/1.json
    url(r'^gambler/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        PartidoDetail.as_view(),
        name='partido_detail_conneg'),

    # Create a partido: /gambler/gambler/create/
    url(r'^gambler/create/$',
        PartidoCreate.as_view(),
        name='partido_create'),

    # Edit partido details, ex: /gambler/gambler/1/edit/
    url(r'^gambler/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Partido,
            form_class=PartidoForm,
            template_name='gambler/form.html'),
        name='partido_edit'),

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
