# Generated by Django 3.0.9 on 2020-08-12 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laptop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LaptopSpecs',
            new_name='LaptopSpec',
        ),
    ]