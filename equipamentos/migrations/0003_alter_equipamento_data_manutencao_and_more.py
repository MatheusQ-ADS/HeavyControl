# Generated by Django 5.2.3 on 2025-06-15 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipamentos", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipamento",
            name="data_manutencao",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="equipamento",
            name="horimetro_manutencao",
            field=models.IntegerField(default=0),
        ),
    ]
