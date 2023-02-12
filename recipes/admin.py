from django.contrib import admin

from recipes.models.ingredient import Ingredient
from recipes.models.recipe import Recipe
from recipes.models.recipe_ingredient_unit import RecipeIngredientUnit
from recipes.models.tag import Tag
from recipes.models.groupModel import groupModel
from recipes.models.contact import Students
from recipes.models.unit import Unit
from recipes.models.event import Event
from recipes.models.groupMembership import GroupMembership
from recipes.models.item import Item




# Register your models here.
admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
admin.site.register(groupModel)
admin.site.register(Students)
admin.site.register(Event)
admin.site.register(GroupMembership)
admin.site.register(Item)


