from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import logging # for logging
import os
import uuid
from django.conf import settings  # Import settings
from PIL import Image  # Import Image from PIL

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

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default="images/profile.png", upload_to=PathAndRename("profile_pictures"))
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

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