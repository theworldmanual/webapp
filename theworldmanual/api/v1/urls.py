from django.urls import path

from . import views

app_name = 'v1'

urlpatterns = [
    path('get-categories/<int:world_id>', views.ListCategories.as_view()),
    path('get-page/<int:page_id>/rendered', views.get_rendered_page),
]
