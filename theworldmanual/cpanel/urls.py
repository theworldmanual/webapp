from django.urls import path

from . import views

app_name = 'cpanel'

urlpatterns = [
    path('', views.worlds_index, name='worlds-index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('worlds/<int:world_id>/', views.world_detail, name='world-detail'),
]
