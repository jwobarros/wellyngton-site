from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.

class Tag(models.Model):
    """Model definition for Tag."""

    name = models.CharField(verbose_name="Nome", max_length=50, unique=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(verbose_name="Titulo", max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    summary = RichTextField(verbose_name="Resumo")
    image = models.FileField(upload_to='uploads/%Y/%m/%d/')
    content =  RichTextField(verbose_name="Conteúdo")
    tags = models.ManyToManyField(Tag, related_name="tags")
    public = models.BooleanField(verbose_name="Postagem pública", default=False)
    created_at = models.DateField(verbose_name="Postado em", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
        ordering = ['-created_at']
    
    def get_related(self):
        related = Post.objects.filter(tags__in=self.tags.all()).distinct().exclude(id=self.id)
        return related

    def __str__(self):
        """Unicode representation of Post."""
        return self.title