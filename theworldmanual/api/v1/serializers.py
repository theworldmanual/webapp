from django.urls import reverse
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from theworldmanual.world.models import PageTreeElement


class CategorySerializer(ModelSerializer):
    parent = SerializerMethodField()
    text = SerializerMethodField()
    icon = SerializerMethodField()
    a_attr = SerializerMethodField()

    class Meta:
        model = PageTreeElement
        fields = ('id', 'text', 'a_attr', 'icon', 'parent')

    @classmethod
    def get_parent(cls, obj):
        return obj.parent_id or '#'

    @staticmethod
    def get_text(obj):
        return obj.title or obj.page and obj.page.title or obj.world.title

    @staticmethod
    def get_icon(obj):
        return obj.page and 'fa ' + obj.page.template.icon

    @staticmethod
    def get_a_attr(obj):
        return {
            'data-type': 'page' if obj.page else 'category' if obj.parent else 'world',
            'data-page': obj.page_id,
            'data-edit-url': reverse('cpanel:page-edit', args=[obj.page_id]) if obj.page else None,
        }
