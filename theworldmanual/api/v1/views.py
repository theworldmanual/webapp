from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView

from theworldmanual.api.v1.serializers import CategorySerializer
from theworldmanual.world.models import PageTreeElement, Page


class ListCategories(ListAPIView):
    serializer_class = CategorySerializer
    model = PageTreeElement

    def get_queryset(self):
        return PageTreeElement.objects.filter(**self.kwargs)


def get_rendered_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    template = page.template
    chunks = []
    sidebar_chunks = []
    for group in template.data.get('groups', []):
        group_chunks = []
        for field in group.get('fields', []):
            lookup_key = f'{group["code"]}.{field["code"]}'
            value = page.data.get(lookup_key)
            if value:
                if field.get('position', 'main') == 'sidebar':
                    sidebar_chunks.append((field['title'], value))
                else:
                    group_chunks.append((field['title'], value))
        if group_chunks:
            chunks.append((group["title"], group_chunks))
    context = {
        'title': page.title,
        'category_icon': page.template.icon,
        'category': page.template.title,
        'main': chunks,
        'sidebar': sidebar_chunks,
    }
    return render(request, 'api_v1/rendered_page.html', context)
