from django.shortcuts import render, get_object_or_404

from theworldmanual.world.models import World


def get_explorer_view(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    return render(request, 'explorer/base.html', {'world': world})
