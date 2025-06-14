# Generated by Django 4.1.7 on 2023-02-27 20:02

import core.enums
import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AmountIngredient",
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
                    "amount",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(
                                core.enums.Limits["MIN_COOKING_TIME"],
                                "Введите количество!",
                            ),
                            django.core.validators.MaxValueValidator(
                                core.enums.Limits["MAX_LEN_USERS_CHARFIELD"],
                                "Слишком много!",
                            ),
                        ],
                        verbose_name="Количество",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингридиент",
                "verbose_name_plural": "Количество ингридиентов",
                "ordering": ("recipe",),
            },
        ),
        migrations.CreateModel(
            name="Carts",
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
                        auto_now_add=True, verbose_name="Дата добавления"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингридиенты рецепта в списке покупок",
                "verbose_name_plural": "Ингридиенты рецептов в списке покупок",
            },
        ),
        migrations.CreateModel(
            name="Favorites",
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
                        auto_now_add=True, verbose_name="Дата добавления"
                    ),
                ),
            ],
            options={
                "verbose_name": "Избранный рецепт",
                "verbose_name_plural": "Избранные рецепты",
            },
        ),
        migrations.CreateModel(
            name="Ingredient",
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
                    "name",
                    models.CharField(max_length=64, verbose_name="Ингридиент"),
                ),
                (
                    "measurement_unit",
                    models.CharField(
                        max_length=24, verbose_name="Единицы измерения"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингридиент",
                "verbose_name_plural": "Ингридиенты",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Recipe",
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
                    "name",
                    models.CharField(
                        max_length=64, verbose_name="Название блюда"
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата публикации"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="recipe_images/",
                        verbose_name="Изображение блюда",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        max_length=5000, verbose_name="Описание блюда"
                    ),
                ),
                (
                    "cooking_time",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, "Ваше блюдо уже готово!"
                            ),
                            django.core.validators.MaxValueValidator(
                                300, "Очень долго ждать..."
                            ),
                        ],
                        verbose_name="Время приготовления",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
                "ordering": ("-pub_date",),
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                    "name",
                    models.CharField(
                        max_length=64,
                        unique=True,
                        validators=[
                            core.validators.OneOfTwoValidator(
                                field="Имя тэга"
                            )
                        ],
                        verbose_name="Тэг",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        max_length=7, unique=True, verbose_name="Цвет"
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        max_length=64, unique=True, verbose_name="Идентификатор тэга"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
                "ordering": ("name",),
            },
        ),
    ]
