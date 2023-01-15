from django.db import models

class LibModel(models.Model):
    title = models.CharField(max_length=70, blank=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.title}"


class ProjModel(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to="")
    description = models.CharField(max_length=400, blank=True)
    libraries = models.ManyToManyField(LibModel)
    slug = models.SlugField(null=True)

    def __str__(self):
        return f"title: {self.title}"
