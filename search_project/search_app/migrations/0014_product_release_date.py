# Generated by Django 5.1.1 on 2024-12-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
