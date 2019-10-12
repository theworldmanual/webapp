from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cpanel/', include('theworldmanual.cpanel.urls', namespace='cpanel')),
]
