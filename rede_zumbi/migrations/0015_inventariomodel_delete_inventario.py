# Generated by Django 4.2 on 2023-04-16 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rede_zumbi", "0014_remove_inventario_item1_remove_inventario_item2_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="InventarioModel",
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
                    "item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rede_zumbi.itemsmodel",
                    ),
                ),
                (
                    "nome_sobrevivente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Inventario",
                        to="rede_zumbi.sobrevivente",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Inventario",
        ),
    ]
