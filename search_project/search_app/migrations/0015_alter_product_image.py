# Generated by Django 5.1.1 on 2024-12-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0014_product_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
