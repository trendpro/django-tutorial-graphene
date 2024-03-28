import django_filters
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Category, Ingredient


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        fields = ["id", "name", "ingredients"]
        interfaces = (relay.Node,)


class CategoryFilterSet(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ["name"]


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "notes": ["exact", "icontains"],
            "category": ["exact"],
            "category__name": ["exact"],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    # all_categories = DjangoFilterConnectionField(CategoryNode)
    all_categories = DjangoFilterConnectionField(
        CategoryNode, filterset_class=CategoryFilterSet
    )

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
