# Generated by Django 4.0.4 on 2022-04-22 04:29

from django.db import migrations, models
import dream_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleepy',
            name='sleey_img',
            field=models.ImageField(null=True, upload_to=dream_api.models.upload_path),
        ),
        migrations.AlterField(
            model_name='sleepy',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]