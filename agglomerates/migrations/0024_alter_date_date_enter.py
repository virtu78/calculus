# Generated by Django 5.1.2 on 2024-12-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agglomerates", "0023_alter_date_date_enter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="date",
            name="date_enter",
            field=models.DateField(null=True),
        ),
    ]
