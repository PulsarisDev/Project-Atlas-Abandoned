URIRoot = 'api/yggdrasil/'

#region
from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

#endregion

urlpatterns = [
    url(r'^$', app.views.home),
#    url(r'^register$', app.views.home),
#    url(r'^login$', app.views.home),
#    url(r'^changepw$', app.views.home),
    url(r'^{}$'.format(URIRoot), app.views.home),
    url(r'^{}authserver/authenticate$'.format(URIRoot), app.views.home),
    url(r'^{}authserver/refresh$'.format(URIRoot), app.views.home),
    url(r'^{}authserver/vaildate$'.format(URIRoot), app.views.home),
    url(r'^{}authserver/invalidate$'.format(URIRoot), app.views.home),
    url(r'^{}authserver/signout$'.format(URIRoot), app.views.home),
    url(r'^{}sessionserver/session/minecraft/join$'.format(URIRoot), app.views.home),
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
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
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
