# Generated by Django 4.2.6 on 2023-11-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_alter_contact_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/contact_images/%Y/%m'),
        ),
    ]
