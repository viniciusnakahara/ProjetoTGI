# Generated by Django 4.0.4 on 2022-07-26 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analises', '0003_alter_amostra_horario_fim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='horario_fim',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 20, 37, 38, 93275)),
        ),
    ]
