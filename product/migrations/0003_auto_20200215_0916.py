# Generated by Django 3.0.3 on 2020-02-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200215_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Titulo'),
        ),
    ]
