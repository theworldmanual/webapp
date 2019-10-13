from django.urls import path

from . import views

app_name = 'cpanel'

urlpatterns = [
    path('', views.worlds_index, name='worlds-index'),
    path('worlds/<int:world_id>', views.world_dashboard, name='world-detail'),
    path('worlds/<int:world_id>/new-page/<int:template_id>', views.new_page, name='page-new'),
    path('worlds/<int:world_id>/pages', views.world_dashboard, name='world-pages'),
    path('pages/<int:page_id>', views.edit_page, name='page-edit'),
    path('pages/<int:page_id>/update', views.update_page, name='page-update'),
]
