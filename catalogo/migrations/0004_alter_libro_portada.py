# Generated by Django 5.1.7 on 2025-04-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_libro_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='media/portada/'),
        ),
    ]
