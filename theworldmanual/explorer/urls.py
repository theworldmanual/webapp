from django.urls import path

from . import views

app_name = 'explorer'

urlpatterns = [
    path('<int:world_id>', views.get_explorer_view),
]
