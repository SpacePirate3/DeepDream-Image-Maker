# Generated by Django 4.0.4 on 2022-04-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_api', '0003_remove_sleepy_sleey_img_alter_sleepy_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleepy',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]