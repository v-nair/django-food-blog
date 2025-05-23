from django import forms
from .models import Recipe
from django.core.exceptions import ValidationError
from PIL import Image
import logging # for logging

logger = logging.getLogger(__name__)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'author', 'description', 'image', 'cooking_time', 'servings', 'tags')

    def clean_image(self):
        logger.debug(f"Processing clean_image")
        image = self.cleaned_data.get('image')
        if image:
            logger.debug(f"Image name: {image.name}")
            logger.debug(f"Image size: {image.size}")
            logger.debug(f"Image content type: {image.content_type}")
            try:
                img = Image.open(image)
                logger.debug(f"Open Image")
                img.verify()  # Validate the image file
                logger.debug(f"Verify Image")
            except Exception:
                logger.debug(f"Uploaded file is not a valid image")
                raise ValidationError("Uploaded file is not a valid image.")
        return image