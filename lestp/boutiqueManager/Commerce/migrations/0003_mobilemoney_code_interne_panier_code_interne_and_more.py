# Generated by Django 5.1.3 on 2025-02-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0002_statistique'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilemoney',
            name='code_interne',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='panier',
            name='code_interne',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vente',
            name='code_interne',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
