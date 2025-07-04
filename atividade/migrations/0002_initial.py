# Generated by Django 5.2.3 on 2025-06-15 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("atividade", "0001_initial"),
        ("equipamentos", "0001_initial"),
        ("local", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="atividade",
            name="equipamento",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="equipamentos.equipamento",
            ),
        ),
        migrations.AddField(
            model_name="atividade",
            name="local",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="local.local"
            ),
        ),
    ]
