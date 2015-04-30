# Create your views here.
from django.core import serializers
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView

from gambler.models import Partido, Apuesta, Equipo
from gambler.forms import ApuestaForm

class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        else:
            return super(ConnegResponseMixin, self).render_to_response(context)

class PartidoList(ListView, ConnegResponseMixin):
    model = Partido
    context_object_name = 'latest_partido_list'
    template_name = 'gambler/partido_list.html'

class EquipoList(ListView, ConnegResponseMixin):
    model = Equipo
    context_object_name = 'latest_equipo_list'
    template_name = 'gambler/equipo_list.html'


class PartidoDetail(DetailView, ConnegResponseMixin):
    model = Partido
    template_name = 'gambler/partido_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PartidoDetail, self).get_context_data(**kwargs)
        return context

class EquipoDetail(DetailView, ConnegResponseMixin):
    model = Equipo
    template_name = 'gambler/partido_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetail, self).get_context_data(**kwargs)
        return context

class ApuestaCreate(CreateView):
    model = Apuesta
    template_name = 'gambler/form.html'
    form_class = ApuestaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.partido = Partido.objects.get(id=self.kwargs['pk'])
        return super(ApuestaCreate, self).form_valid(form)

