from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from theworldmanual.api.v1.serializers import CategorySerializer
from theworldmanual.world.models import PageTreeElement, Page


class ListCategories(ListAPIView):
    serializer_class = CategorySerializer
    model = PageTreeElement

    def get_queryset(self):
        return PageTreeElement.objects.filter(**self.kwargs)


def get_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    template = page.template
    main_chunks = []
    sidebar_chunks = []
    for group in template.data.get('groups', []):
        group_chunks = []
        for field in group.get('fields', []):
            lookup_key = f'{group["code"]}.{field["code"]}'
            value = page.data.get(lookup_key)
            if value:
                if field.get('position', 'main') == 'sidebar':
                    sidebar_chunks.append({
                        'title': field['title'],
                        'value': value,
                    })
                else:
                    group_chunks.append({
                        'title': field['title'],
                        'value': value,
                    })
        if group_chunks:
            main_chunks.append({
                'title': group["title"],
                'fields': group_chunks,
            })
    context = {
        'title': page.title,
        'category_icon': page.template.icon,
        'category': page.template.title,
        'main': main_chunks,
        'sidebar': sidebar_chunks,
    }
    return JsonResponse(context)
