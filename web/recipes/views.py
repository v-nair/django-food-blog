from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm

class RecipeListView(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "recipes/recipe_list.html"
    paginate_by = 21

    def get_queryset(self):
        qs = (
            Recipe.objects
            .select_related("author")
            .prefetch_related("tags")
            .order_by("-created_at")
        )
        tag    = self.request.GET.get("tag")
        search = self.request.GET.get("q")
        user   = self.request.GET.get("user")
        if tag:
            qs = qs.filter(tags__name=tag)
        if search:
            qs = qs.filter(title__icontains=search)
        if user:
            qs = qs.filter(author__id=user)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page_obj"] = ctx["page_obj"]
        # preserve any query params
        ctx["query_params"] = self.request.GET.urlencode()
        return ctx

def recipe_list_api(request):
    """
    AJAX endpoint: same filters + page number as ListView.
    Returns a JSON payload with rendered HTML fragment + has_next flag.
    """
    view = RecipeListView()
    view.request = request
    qs = view.get_queryset()
    page = request.GET.get("page", 1)
    paginator = Paginator(qs, 21)
    page_obj = paginator.get_page(page)

    html = render_to_string(
        "recipes/partials/recipe_cards.html",
        {"recipes": page_obj},
        request=request
    )
    return JsonResponse({
        "html": html,
        "has_next": page_obj.has_next()
    })


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("recipes:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("recipes:index")

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipes:index")


