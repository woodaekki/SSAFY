from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crawlings/', include("contentfetch.urls")),
    path('accounts/', include("accounts.urls")),
    # path('pjt04/', RedirectView.as_view(url='/pjt04/index/')),
]
