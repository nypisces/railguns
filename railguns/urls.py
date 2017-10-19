from django.apps.registry import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import RedirectView
from django.views.i18n import JavaScriptCatalog
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .rest_framework.views import download_url, upload_params


# 系统自带
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog')  # https://docs.djangoproject.com/en/dev/topics/i18n/translation/#note-on-performance
]
# 第三方
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('developer/documentation/', include_docs_urls(title='{} API'.format(_('app_name')), public=False)),
    # path('search/', include('haystack.urls'))
]
# RailgunS
urlpatterns += [
    re_path(r'download_url/(?P<pk>\w+)/$', download_url, name='download_url'),
    re_path(r'upload_params/(?P<pk>\w+)/$', upload_params, name='upload_params'),
    path('favicon.ico', RedirectView.as_view(url='{}favicon.ico'.format(settings.STATIC_URL), permanent=True))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if apps.is_installed('rosetta'):
    urlpatterns += [path('rosetta/', include('rosetta.urls'))]
