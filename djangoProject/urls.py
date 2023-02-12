"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from recipes.views.JoinGroup import JoinGroupView
from recipes.views.createGroup import CreateGroupView
from recipes.views.createEvent import CreateEventView
from recipes.views.createItem import ItemCreateView
from recipes.views.eventByevent import EventsView
from recipes.views.json.group_list import GroupListJsonView
from recipes.views.login import UserLoginView
from recipes.views.panel import Panel
from recipes.views.event import eventView
from recipes.views.index import IndexView
from recipes.views.recipe.detail import RecipeDetailView
from recipes.views.recipe.list import RecipeListView
from recipes.views.recipe.search import RecipeSearchView
from recipes.views.recipe.search_by_ingredient import RecipeSearchByIngredientView
from recipes.views.register_form import RegisterFormView
from recipes.views.tag.create import TagCreateView
from recipes.views.tag.detail import TagDetailView
from recipes.views.tag.list import TagListView
from recipes.views.tag.update import TagUpdateView
from recipes.views.eventByGroup import GroupEventsListView
from recipes.views.Group_detail_view import GroupInfoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('group', GroupListJsonView.as_view(), name='group'),
    path('group/create', CreateGroupView.as_view(), name='group_create'),
    path('item/create/<int:group_id>/<int:event_id>/', ItemCreateView.as_view(), name='item_create'),
    path('group/join', JoinGroupView.as_view(), name='groupJoin'),
    path('group_details/', GroupInfoView.as_view(), name='group_details'),
    path('panel/group/<int:group_id>/create/event/', CreateEventView.as_view(), name='createEvent'),
    path('panel/group/<int:group_id>/events/', GroupEventsListView.as_view(), name='group_event'),
    path('panel/group/<int:group_id>/events/<int:event_id>/', EventsView.as_view(), name='eventView'),
    path('panel/', Panel.as_view(), name='panel'),
    path('event/list', eventView.as_view(), name='eventlist'),
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/detail/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/search/<str:search>', RecipeSearchView.as_view(), name='recipe_search'),
    path('recipes/search/by-ingredient/<str:search>', RecipeSearchByIngredientView.as_view(), name='recipe_search_by_ingredient'),
    path('tags/list', TagListView.as_view(), name='tag_list'),
    path('tags/detail/<int:pk>', TagDetailView.as_view(), name='tag_detail'),
    path('tags/create', TagCreateView.as_view(), name='tag_create'),
    path('tags/update/<int:pk>', TagUpdateView.as_view(), name='tag_update'),
    path('json/recipes/list', RecipeListView.as_view(), name='recipe_list_json'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
