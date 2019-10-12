from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from theworldmanual.world.models import World, PageTemplate


def worlds_index(request):
    context = {
        'worlds': World.objects.all(),
    }
    return render(request, 'worlds/index.html', context)


def world_detail(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    context = {
        'world': world,
        'page_templates': PageTemplate.objects.all(),
    }
    return render(request, 'worlds/edit.html', context)


def dashboard(request):
    context = {
    }
    return render(request, 'dashboard.html', context)
