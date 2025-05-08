from django.shortcuts import render
from django.http import JsonResponse
from recipes.models import Featured, Recipe

def landing_page(request):
    # Grab the 3 featured entries, with their related Recipe
    landing = (
        Featured.objects
        .select_related('recipe')
        .order_by('-created_at')[:3]
    )

    # Grab the 12 most recent recipes, prefetching tags
    latest = (
        Recipe.objects
        .prefetch_related('tags')
        .order_by('-created_at')[:12]
    )
    context = {
        "landing": landing,
        "latest": latest
    }
    return render(request, 'landing.html', context)

# health check
def health_view(request):
    return JsonResponse({"status": "ok"}, status=200)

