# Generated by Django 4.2 on 2023-04-16 19:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rede_zumbi", "0017_alter_inventariomodel_quantidade"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comerciozumbimodel",
            old_name="item1_ngc1",
            new_name="itens_ngc1",
        ),
        migrations.RenameField(
            model_name="comerciozumbimodel",
            old_name="item1_ngc2",
            new_name="itens_ngc2",
        ),
        migrations.RemoveField(
            model_name="comerciozumbimodel",
            name="item2_ngc1",
        ),
        migrations.RemoveField(
            model_name="comerciozumbimodel",
            name="item2_ngc2",
        ),
    ]