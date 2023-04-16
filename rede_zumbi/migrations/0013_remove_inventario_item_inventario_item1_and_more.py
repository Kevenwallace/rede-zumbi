# Generated by Django 4.2 on 2023-04-15 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rede_zumbi", "0012_alter_sobrevivente_pontosdeinfectacao"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inventario",
            name="item",
        ),
        migrations.AddField(
            model_name="inventario",
            name="item1",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_um",
                to="rede_zumbi.itemsmodel",
            ),
        ),
        migrations.AddField(
            model_name="inventario",
            name="item2",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_dois",
                to="rede_zumbi.itemsmodel",
            ),
        ),
        migrations.AddField(
            model_name="inventario",
            name="item3",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_tres",
                to="rede_zumbi.itemsmodel",
            ),
        ),
        migrations.AddField(
            model_name="inventario",
            name="item4",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_quatro",
                to="rede_zumbi.itemsmodel",
            ),
        ),
    ]
