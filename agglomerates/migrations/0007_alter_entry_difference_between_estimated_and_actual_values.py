# Generated by Django 5.1.2 on 2024-11-25 07:42

import django.db.models.expressions
import django.db.models.functions.math
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agglomerates", "0006_entry_actual_value_of_agglomeration_output_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="difference_between_estimated_and_actual_values",
            field=models.GeneratedField(
                db_persist=False,
                expression=django.db.models.functions.math.Round(
                    django.db.models.expressions.CombinedExpression(
                        models.F("output_agglomerate"),
                        "-",
                        models.F("actual_value_of_agglomeration_output"),
                    ),
                    precision=1,
                ),
                output_field=models.BigIntegerField(),
                verbose_name="Абсолютная разница между расчетным и фактическим значениями",
            ),
        ),
    ]
