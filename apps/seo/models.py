from django.db import models


class SEOMetadata(models.Model):
    entity_type = models.CharField(max_length=50)
    entity_id = models.BigIntegerField()

    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    meta_description = models.TextField(
        blank=True,
        null=True,
    )

    canonical_url = models.URLField(
        max_length=1000,
        blank=True,
        null=True,
    )

    og_image = models.ForeignKey(
        "media.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="seo_metadata",
    )

    no_index = models.BooleanField(default=False)



    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["entity_type", "entity_id"],
                name="unique_seo_entity",
            )
        ]

    def __str__(self):
        return self.meta_title or f"{self.entity_type} #{self.entity_id}"
