# Generated by Django 2.2.6 on 2019-10-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0008_provider_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main_Provider/'),
        ),
    ]
