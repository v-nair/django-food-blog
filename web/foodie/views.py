from django.shortcuts import render
from django.http import JsonResponse


def home_view(request):
    context = {
        
    }
    return render(request, 'index.html', context)

# health check
def health_view(request):
    return JsonResponse({"status": "ok"}, status=200)

