# Generated by Django 4.0 on 2022-08-16 16:12

import DevSearch.utils.uploads
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_project_featured_image_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default/image-default.jpg', null=True, upload_to=DevSearch.utils.uploads.project_image_upload_path),
        ),
    ]
