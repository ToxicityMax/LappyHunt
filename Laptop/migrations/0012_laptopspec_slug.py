# Generated by Django 3.0.9 on 2020-09-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laptop', '0011_auto_20200922_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptopspec',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]