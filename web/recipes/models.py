import os
import uuid
import logging
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.deconstruct import deconstructible
from PIL import Image

# Initialize logger
logger = logging.getLogger(__name__)

@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return os.path.join(self.sub_path, filename)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Featured(models.Model):
    title     = models.CharField(max_length=200)
    image     = models.ImageField(
        upload_to=PathAndRename('landing/images/'),
        default='landing/images/placeholder.png',
        blank=True, null=True,
    )
    recipe    = models.ForeignKey(    # renamed from recipe_id
        'Recipe',
        on_delete=models.CASCADE,
        related_name='featured_entries',
        blank=True, null=True,
    )
    subtitle  = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.recipe.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            try:
                img = Image.open(img_path)
                if img.height > 800 or img.width > 800:
                    img.thumbnail((800, 800))
                    img.save(img_path)
            except Exception as e:
                logger.error(f"Error processing image {self.image.name}: {e}")

class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to=PathAndRename('recipes/images/'),
        default='recipes/images/placeholder.png',
        blank=True,
        null=True,
    )
    description = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Minutes to cook")
    servings = models.PositiveSmallIntegerField(default=1)
    tags = models.ManyToManyField(Tag, blank=True, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            try:
                img = Image.open(img_path)
                if img.height > 800 or img.width > 800:
                    img.thumbnail((800, 800))
                    img.save(img_path)
            except Exception as e:
                logger.error(f"Error processing image {self.image.name}: {e}")


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="items", on_delete=models.CASCADE)
    item_type = models.CharField(max_length=50)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_type}: {self.value}"


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.recipe}"


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ratings", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("recipe", "user"),)

    def __str__(self):
        return f"{self.stars} stars by {self.user} on {self.recipe}"
