from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.education.models import (
    EducationCategory,
    EducationContent,
    EducationMedia,
    EducationVideo,
)
from apps.industries.models import Industry
from apps.products.models import (
    Product,
    ProductCategories,
    ProductImages,
    ProductSpec,
    ProductVideos,
)
from apps.services.models import Service

_initialized = False


def _clear_related_cache(*args, **kwargs):
    cache.clear()


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def invalidate_product_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=ProductCategories)
@receiver(post_delete, sender=ProductCategories)
def invalidate_product_category_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=ProductImages)
@receiver(post_delete, sender=ProductImages)
def invalidate_product_images_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=ProductVideos)
@receiver(post_delete, sender=ProductVideos)
def invalidate_product_videos_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=ProductSpec)
@receiver(post_delete, sender=ProductSpec)
def invalidate_product_specs_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=Industry)
@receiver(post_delete, sender=Industry)
def invalidate_industry_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=EducationContent)
@receiver(post_delete, sender=EducationContent)
def invalidate_education_content_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=EducationCategory)
@receiver(post_delete, sender=EducationCategory)
def invalidate_education_category_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=EducationMedia)
@receiver(post_delete, sender=EducationMedia)
def invalidate_education_media_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=EducationVideo)
@receiver(post_delete, sender=EducationVideo)
def invalidate_education_video_cache(sender, **kwargs):
    _clear_related_cache()


@receiver(post_save, sender=Service)
@receiver(post_delete, sender=Service)
def invalidate_service_cache(sender, **kwargs):
    _clear_related_cache()


def register_cache_invalidation_signals():
    global _initialized
    if _initialized:
        return
    _initialized = True
