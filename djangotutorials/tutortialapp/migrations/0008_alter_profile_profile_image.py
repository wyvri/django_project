# Generated by Django 4.2.11 on 2024-05-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutortialapp', '0007_alter_profile_profile_image_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='cat.png', null=True, upload_to=''),
        ),
    ]
