# Generated by Django 5.1.2 on 2024-12-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agglomerates", "0016_remove_date_date_enter"),
    ]

    operations = [
        migrations.AddField(
            model_name="date",
            name="date_enter",
            field=models.DateField(blank=True, null=True),
        ),
    ]
