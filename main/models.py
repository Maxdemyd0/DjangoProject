from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'categories'

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, blank=True)
    icon_url = models.URLField()

    developer = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        related_name="developed_games"
    )

    publisher = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        related_name="published_games"
    )

    added_by = models.TextField(null=True, blank=True)

    gameplay_video = models.FileField(
        upload_to="game_videos/",
        blank=True,
        null=True
    )

    site_url = models.URLField(blank=True)

    class Meta:
        db_table = 'games'