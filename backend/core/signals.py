from pathlib import Path

from django.db.models.signals import post_delete
from django.dispatch import receiver
from recipes.models import Recipe


@receiver(post_delete, sender=Recipe)
def delete_image(sender: Recipe, instance: Recipe, *a, **kw) -> None:
    """Удаление картинки при удалении рецепта"""
    image = Path(instance.image.path)
    if image.exists():
        image.unlink()
