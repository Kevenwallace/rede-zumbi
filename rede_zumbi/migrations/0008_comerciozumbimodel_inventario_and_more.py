# Generated by Django 4.2 on 2023-04-11 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rede_zumbi", "0007_remove_niveldeinfecao_infectado_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComercioZumbiModel",
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
                ("item1_ngc1", models.CharField(max_length=15)),
                ("item2_ngc1", models.CharField(max_length=15)),
                ("item1_ngc2", models.CharField(max_length=15)),
                ("item2_ngc2", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Inventario",
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
            ],
        ),
        migrations.RemoveField(
            model_name="sobrevivente",
            name="inventario",
        ),
        migrations.AddField(
            model_name="items",
            name="nome",
            field=models.CharField(default=1, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="items",
            name="valor",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="NivelDeInfecao",
        ),
        migrations.AddField(
            model_name="inventario",
            name="item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rede_zumbi.items",
            ),
        ),
        migrations.AddField(
            model_name="inventario",
            name="sobrrevivente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="rede_zumbi.sobrevivente",
            ),
        ),
        migrations.AddField(
            model_name="comerciozumbimodel",
            name="negociador_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="negoiciado_um",
                to="rede_zumbi.sobrevivente",
            ),
        ),
        migrations.AddField(
            model_name="comerciozumbimodel",
            name="negociador_2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="negociador_dois",
                to="rede_zumbi.sobrevivente",
            ),
        ),
    ]
