# Generated by Django 4.2.6 on 2023-11-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_contact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
