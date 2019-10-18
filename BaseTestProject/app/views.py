"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.views.generic import TemplateView, View, ListView, UpdateView, DeleteView, CreateView
from app.models import Persona
from app.forms import PersonaForm
from django.urls import reverse_lazy


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )



class PersonaListView(ListView):
    template_name = 'persona/persona_list.html'
    model = Persona


class PersonaCreateView(CreateView):
    template_name = 'persona/persona.html'
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('persona-list')


class PersonaEditView(UpdateView):
    template_name = 'persona/persona.html'
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('persona-list')


class PersonaDeleteView(DeleteView):
    template_name = 'persona/persona_delete.html'
    model = Persona
    success_url = reverse_lazy('persona-list')