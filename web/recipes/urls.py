from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.RecipeListView.as_view(), name="index"), # the main list with infinite scroll
    path("api/", views.recipe_list_api, name="api_list"), # AJAX endpoint for page fragments
    path("add/", views.RecipeCreateView.as_view(), name="add"),
    path("<int:pk>/", views.RecipeDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.RecipeUpdateView.as_view(), name="edit"),
]
