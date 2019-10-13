from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from theworldmanual.world.models import World, PageTemplate, Page


def worlds_index(request):
    context = {
        'worlds': World.objects.all(),
    }
    return render(request, 'worlds/index.html', context)


def world_dashboard(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    context = {
        'world': world,
        'page_templates': PageTemplate.objects.all(),
        'recent_pages': Page.objects.filter(world=world).order_by('-updated_at')[:10],
    }
    return render(request, 'worlds/dashboard.html', context)


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


def update_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    # We mark real data fields with prefixed $
    new_title = request.POST.get('page_title', '')
    clean_data = {
        key[1:]: value
        for key, value in request.POST.items()
        if key.startswith('$')
        if value
    }
    page.title = new_title
    page.data = clean_data
    page.save()
    return redirect(reverse('cpanel:page-edit', kwargs={'page_id': page_id}))


def list_pages(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    pages = Page.objects.filter(world=world).order_by('title')
    context = {
        'world': world,
        'pages': pages,
    }
    return render(request, 'page/categories.html', context)
