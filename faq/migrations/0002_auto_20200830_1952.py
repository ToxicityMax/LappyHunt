# Generated by Django 3.0.9 on 2020-08-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faql',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
