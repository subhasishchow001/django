# Generated by Django 4.1.3 on 2022-12-04 15:35

from django.db import migrations, models
import portfolioapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_alter_blogposts_backimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='backimage',
            field=models.ImageField(null=True, upload_to=portfolioapp.models.upload_path),
        ),
    ]
