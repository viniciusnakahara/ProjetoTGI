# Generated by Django 4.0.4 on 2022-07-26 17:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NomeAmostra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_amostra', models.CharField(default='10', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_dia', models.DateTimeField(auto_now_add=True)),
                ('ph', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_dia', models.DateTimeField(auto_now_add=True)),
                ('temperatura', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeira_etapa', models.BooleanField(default=0)),
                ('horario_fim', models.DateTimeField(default=datetime.datetime(2022, 7, 26, 20, 35, 1, 838110))),
                ('nome', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Analises.nomeamostra')),
                ('ph_fk', models.ForeignKey(default=7.0, on_delete=django.db.models.deletion.CASCADE, to='Analises.ph')),
                ('temperatura_fk', models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='Analises.temperatura')),
                ('usuario_fk', models.OneToOneField(default='10', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
