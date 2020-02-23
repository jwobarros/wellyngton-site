from django.db import models
from django.core.paginator import Paginator

# Create your models here.

class Category(models.Model):
    """Model definition for Category."""

    title = models.CharField(verbose_name="Titulo", max_length=60, unique=True)
    summary = models.TextField(verbose_name="Descrição")
    created_at = models.DateTimeField(verbose_name="Adicionado em", auto_now_add=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['title']
    
    def category_id(self):
        """Used in frontend to make carousels to each category"""
        return self.title.replace(" ", '')


    def products_pagination(self):
        objects = Product.objects.filter(category__pk=self.pk, active=True)
        return Paginator(objects, 3)

    def __str__(self):
        """Unicode representation of Category."""
        return self.title


class Product(models.Model):
    """Model definition for Product."""

    category = models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Titulo", max_length=60)
    summary = models.TextField(verbose_name="Descrição")
    price = models.FloatField(verbose_name="Preço")
    link = models.URLField(verbose_name="Link", max_length=300)
    active = models.BooleanField(verbose_name="Ativo")    
    created_at = models.DateTimeField(verbose_name="Adicionado em", auto_now_add=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-created_at']

    def __str__(self):
        """Unicode representation of Product."""
        return self.title

