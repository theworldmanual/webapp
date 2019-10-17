from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cpanel/', include('theworldmanual.cpanel.urls', namespace='cpanel')),
    path('api/', include('theworldmanual.api.urls', namespace='api')),
    path('explorer/', include('theworldmanual.explorer.urls', namespace='explorer')),
]
