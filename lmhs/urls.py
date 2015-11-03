from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from lmhs.views import SimpleSearchForm, Gallery, NewForm, InsertPrincipal
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lmhs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
    url(r'^simple_search/', SimpleSearchForm.as_view()),
    url(r'^new/', login_required(NewForm.as_view())),
    url(r'^insert_principal/', login_required(InsertPrincipal.as_view())),
    url(r'^$', Gallery.as_view()),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)