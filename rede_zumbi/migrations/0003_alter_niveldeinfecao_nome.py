# Generated by Django 4.2 on 2023-04-06 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rede_zumbi', '0002_niveldeinfecao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='niveldeinfecao',
            name='nome',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rede_zumbi.sobrevivente'),
            preserve_default=False,
        ),
    ]