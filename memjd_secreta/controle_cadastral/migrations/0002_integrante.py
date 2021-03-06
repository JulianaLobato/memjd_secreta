# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_cadastral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(default='0', max_length=255, verbose_name='Telefone')),
                ('celular', models.CharField(default='0', max_length=255, verbose_name='Celular')),
                ('observacao', models.TextField(blank=True, null=True)),
                ('doenca', models.TextField(blank=True, null=True)),
                ('tarefa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='controle_cadastral.Tarefa')),
            ],
        ),
    ]
