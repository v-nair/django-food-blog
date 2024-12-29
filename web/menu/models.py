from django.db import models
import os
import logging # for logging
from django.conf import settings  # Import settings
from PIL import Image  # Import Image from PIL
import uuid
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User
from django.urls import reverse

# Initialize logger
logger = logging.getLogger(__name__)

@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Set filename as a random string with the same extension
        filename = f"{uuid.uuid4()}.{ext}"
        # Return the whole path to the file
        return os.path.join(self.sub_path, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=3, default="$")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to=PathAndRename('images/'), default='images/placeholder.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return self.name

    def row(self):
        return f"Item(name='{self.name}', price={self.price}, category='{self.category.name}', is_active={self.is_active})"

    # redirect the url when the item is created
    def get_absolute_url(self):
        return reverse('menu:details', kwargs={'pk': self.pk})
        # return reverse('item-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            try:
                logger.debug(f"Processing image at {img_path}")
                img = Image.open(img_path)
                if img.height > 800 or img.width > 800:
                    output_size = (800, 800)
                    img.thumbnail(output_size)
                    img.save(img_path)
                    logger.debug(f"Image resized and saved at {img_path}")
            except Exception as e:
                # Log the error with the image name
                logger.error(f"Error processing image {self.image.name}: {e}")