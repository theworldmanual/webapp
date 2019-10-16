from rest_framework.generics import ListAPIView

from theworldmanual.api.v1.serializers import CategorySerializer
from theworldmanual.world.models import PageTreeElement


class ListCategories(ListAPIView):
    serializer_class = CategorySerializer
    model = PageTreeElement

    def get_queryset(self):
        return PageTreeElement.objects.filter(**self.kwargs)
