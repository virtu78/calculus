# Generated by Django 5.1.2 on 2024-11-19 11:21

import django.db.models.deletion
import django.db.models.expressions
import django.db.models.functions.math
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Date",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(default="", max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Entry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_added",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата расчета"
                    ),
                ),
                (
                    "titanium_content_in_agglomerate",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Содержание титана в агломерате КГОК:",
                    ),
                ),
                (
                    "mechanical_strength_of_agglomerate",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Механическая (барабанная) прочность агломерата:",
                    ),
                ),
                (
                    "output_in_agglomerate_of_size_class",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Выход в агломерате классаа крупности-40+15мм:",
                    ),
                ),
                (
                    "specific_consumption_of_natural_gas",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Расход природного газа:",
                    ),
                ),
                (
                    "water_consumption_in_drum_pelletizer",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Расход воды в барабанном окомкователе:",
                    ),
                ),
                (
                    "charge_consumption_before_seeding",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Расход шихты до высева:",
                    ),
                ),
                (
                    "exhaust_gas_temperature",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Температура отходящих газов:",
                    ),
                ),
                (
                    "velocity_am",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Скорость агломашины",
                    ),
                ),
                (
                    "jig_bed_weight",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Вес постели общий:",
                    ),
                ),
                (
                    "content_titan_in_source_ore",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Содержание титана в концентрате",
                    ),
                ),
                (
                    "content_of_size_class_in_source_ore",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Содержание в концентрате класса крупности -0,071 мм:",
                    ),
                ),
                (
                    "output_in_limestone_of_size_class",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Выход в известняке класса крупности +3, мм:",
                    ),
                ),
                (
                    "specific_fuel_consumption",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Удельный расход топлива:",
                    ),
                ),
                (
                    "consumption_of_agglomeration_charge_after_seeding",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Расход агломерационной шихты послевысева:",
                    ),
                ),
                (
                    "filling_level_of_bed_bin",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Уровень заполнения бункера постели:",
                    ),
                ),
                (
                    "moisture_content_in_hopper_am",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Влажность шихты в бункере а/м:",
                    ),
                ),
                (
                    "temperature_in_vacuum_chamber_no_eighteen",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Температура в вакуум-камере № 18:",
                    ),
                ),
                (
                    "temperature_in_vacuum_chamber_no_nineteen",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Температура в вакуум-камере № 19:",
                    ),
                ),
                (
                    "output_agglomerate",
                    models.GeneratedField(
                        db_persist=False,
                        expression=django.db.models.functions.math.Round(
                            django.db.models.expressions.CombinedExpression(
                                django.db.models.expressions.CombinedExpression(
                                    django.db.models.expressions.CombinedExpression(
                                        django.db.models.expressions.CombinedExpression(
                                            django.db.models.expressions.CombinedExpression(
                                                django.db.models.expressions.CombinedExpression(
                                                    django.db.models.expressions.CombinedExpression(
                                                        django.db.models.expressions.CombinedExpression(
                                                            django.db.models.expressions.CombinedExpression(
                                                                django.db.models.expressions.CombinedExpression(
                                                                    django.db.models.expressions.CombinedExpression(
                                                                        django.db.models.expressions.CombinedExpression(
                                                                            django.db.models.expressions.CombinedExpression(
                                                                                django.db.models.expressions.CombinedExpression(
                                                                                    django.db.models.expressions.CombinedExpression(
                                                                                        django.db.models.expressions.CombinedExpression(
                                                                                            django.db.models.expressions.CombinedExpression(
                                                                                                django.db.models.expressions.CombinedExpression(
                                                                                                    models.Value(
                                                                                                        714.38
                                                                                                    ),
                                                                                                    "+",
                                                                                                    django.db.models.expressions.CombinedExpression(
                                                                                                        models.Value(
                                                                                                            74.41
                                                                                                        ),
                                                                                                        "*",
                                                                                                        models.F(
                                                                                                            "titanium_content_in_agglomerate"
                                                                                                        ),
                                                                                                    ),
                                                                                                ),
                                                                                                "+",
                                                                                                django.db.models.expressions.CombinedExpression(
                                                                                                    models.Value(
                                                                                                        9.09
                                                                                                    ),
                                                                                                    "*",
                                                                                                    models.F(
                                                                                                        "mechanical_strength_of_agglomerate"
                                                                                                    ),
                                                                                                ),
                                                                                            ),
                                                                                            "+",
                                                                                            django.db.models.expressions.CombinedExpression(
                                                                                                models.Value(
                                                                                                    1.06
                                                                                                ),
                                                                                                "*",
                                                                                                models.F(
                                                                                                    "output_in_agglomerate_of_size_class"
                                                                                                ),
                                                                                            ),
                                                                                        ),
                                                                                        "+",
                                                                                        django.db.models.expressions.CombinedExpression(
                                                                                            models.Value(
                                                                                                23.19
                                                                                            ),
                                                                                            "*",
                                                                                            models.F(
                                                                                                "specific_consumption_of_natural_gas"
                                                                                            ),
                                                                                        ),
                                                                                    ),
                                                                                    "+",
                                                                                    django.db.models.expressions.CombinedExpression(
                                                                                        models.Value(
                                                                                            12.1
                                                                                        ),
                                                                                        "*",
                                                                                        models.F(
                                                                                            "water_consumption_in_drum_pelletizer"
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                                "+",
                                                                                django.db.models.expressions.CombinedExpression(
                                                                                    models.Value(
                                                                                        0.84
                                                                                    ),
                                                                                    "*",
                                                                                    models.F(
                                                                                        "charge_consumption_before_seeding"
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                            "+",
                                                                            django.db.models.expressions.CombinedExpression(
                                                                                models.Value(
                                                                                    3.85
                                                                                ),
                                                                                "*",
                                                                                models.F(
                                                                                    "exhaust_gas_temperature"
                                                                                ),
                                                                            ),
                                                                        ),
                                                                        "+",
                                                                        django.db.models.expressions.CombinedExpression(
                                                                            models.Value(
                                                                                64.37
                                                                            ),
                                                                            "*",
                                                                            models.F(
                                                                                "velocity_am"
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    "+",
                                                                    django.db.models.expressions.CombinedExpression(
                                                                        models.Value(
                                                                            0.21
                                                                        ),
                                                                        "*",
                                                                        models.F(
                                                                            "jig_bed_weight"
                                                                        ),
                                                                    ),
                                                                ),
                                                                "-",
                                                                django.db.models.expressions.CombinedExpression(
                                                                    models.Value(
                                                                        155.15
                                                                    ),
                                                                    "*",
                                                                    models.F(
                                                                        "content_titan_in_source_ore"
                                                                    ),
                                                                ),
                                                            ),
                                                            "-",
                                                            django.db.models.expressions.CombinedExpression(
                                                                models.Value(6.08),
                                                                "*",
                                                                models.F(
                                                                    "content_of_size_class_in_source_ore"
                                                                ),
                                                            ),
                                                        ),
                                                        "-",
                                                        django.db.models.expressions.CombinedExpression(
                                                            models.Value(5.81),
                                                            "*",
                                                            models.F(
                                                                "output_in_limestone_of_size_class"
                                                            ),
                                                        ),
                                                    ),
                                                    "-",
                                                    django.db.models.expressions.CombinedExpression(
                                                        models.Value(2.8),
                                                        "*",
                                                        models.F(
                                                            "specific_fuel_consumption"
                                                        ),
                                                    ),
                                                ),
                                                "-",
                                                django.db.models.expressions.CombinedExpression(
                                                    models.Value(0.68),
                                                    "*",
                                                    models.F(
                                                        "consumption_of_agglomeration_charge_after_seeding"
                                                    ),
                                                ),
                                            ),
                                            "-",
                                            django.db.models.expressions.CombinedExpression(
                                                models.Value(1.82),
                                                "*",
                                                models.F("filling_level_of_bed_bin"),
                                            ),
                                        ),
                                        "-",
                                        django.db.models.expressions.CombinedExpression(
                                            models.Value(81.66),
                                            "*",
                                            models.F("moisture_content_in_hopper_am"),
                                        ),
                                    ),
                                    "-",
                                    django.db.models.expressions.CombinedExpression(
                                        models.Value(1.17),
                                        "*",
                                        models.F(
                                            "temperature_in_vacuum_chamber_no_eighteen"
                                        ),
                                    ),
                                ),
                                "-",
                                django.db.models.expressions.CombinedExpression(
                                    models.Value(1.05),
                                    "*",
                                    models.F(
                                        "temperature_in_vacuum_chamber_no_nineteen"
                                    ),
                                ),
                            ),
                            precision=1,
                        ),
                        output_field=models.BigIntegerField(),
                        verbose_name="Выход аглоотсева, кг/т:",
                    ),
                ),
                (
                    "date",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="agglomerates.date",
                        verbose_name="Группа расчотов",
                    ),
                ),
            ],
        ),
    ]