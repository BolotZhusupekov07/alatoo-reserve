from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    url(r"^auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("", include("reserve.urls")),
]
urlpatterns += [
    url(r"^i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(url(r"^admin/", admin.site.urls))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
