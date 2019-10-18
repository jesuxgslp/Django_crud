"""
Definition of urls for BaseTestProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', app.views.home, name='home'),
    url(r'^$', app.views.PersonaListView.as_view(), name='persona-list'),
    url(r'^persona/create/$', app.views.PersonaCreateView.as_view(), name='persona-create'),
    url(r'^persona/delete/(?P<pk>\d+)/$', app.views.PersonaDeleteView.as_view(), name='persona-delete'),
    url(r'^persona/update/(?P<pk>\d+)/$', app.views.PersonaEditView.as_view(), name='persona-update'),

    url(r'^about', app.views.about, name='about'),
    url(r'^contact', app.views.contact, name='contact'),
    url(r'^app/home', app.views.home, name='home'),
    url(r'^login/$',
        django.contrib.auth.views.LoginView.as_view,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.LogoutView.as_view,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
