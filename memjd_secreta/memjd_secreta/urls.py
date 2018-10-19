from django.conf.urls import include, url
import django.contrib.auth.views
import controle_cadastral.views
import controle_cadastral.forms

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', controle_cadastral.views.index, name='index'),
   # url(r'^memjd_secreta/', include('memjd_secreta.memjd_secreta.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'controle_cadastral/login.html',
            'authentication_form': controle_cadastral.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Entrar',
            },
            'next_page': '/admin',
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/index',
        },
        name='logout'),
]
