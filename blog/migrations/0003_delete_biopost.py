# Generated by Django 5.0.4 on 2024-04-17 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_biopost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BioPost',
        ),
    ]