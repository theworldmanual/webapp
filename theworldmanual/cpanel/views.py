from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from theworldmanual.world.models import World, PageTemplate, Page


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


def new_page(request, world_id, template_id):
    world = get_object_or_404(World, pk=world_id)
    template = get_object_or_404(PageTemplate, pk=template_id)
    page = Page.objects.create(world=world, template=template)
    return redirect(reverse('cpanel:page-edit', kwargs={'page_id': page.pk}))


def edit_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    context = {
        'world': page.world,
        'template': page.template,
        'page': page,
    }
    return render(request, 'page/edit.html', context)
