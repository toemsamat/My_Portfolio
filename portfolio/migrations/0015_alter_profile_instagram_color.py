# Generated by Django 5.1.7 on 2025-05-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_profile_instagram_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instagram_color',
            field=models.CharField(blank=True, default='#C13584', max_length=20),
        ),
    ]
