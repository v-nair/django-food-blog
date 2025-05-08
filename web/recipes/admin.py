from django.contrib import admin
from .models import Tag, Recipe, Comment, Rating

admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Rating)
