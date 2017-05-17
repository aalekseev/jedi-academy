# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Код ордена')),
            ],
            options={
                'verbose_name': 'Тестовое испытание',
                'verbose_name_plural': 'Тестовые испытания',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Джедай',
                'verbose_name_plural': 'Джедаи',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Padawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_app.Candidate')),
                ('jedi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_app.Jedi', verbose_name='')),
            ],
            options={
                'verbose_name': 'Падаван',
                'verbose_name_plural': 'Падаваны',
                'ordering': ('jedi',),
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Планета',
                'verbose_name_plural': 'Планеты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст вопроса')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_app.Exam')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('text',),
            },
        ),
        migrations.AddField(
            model_name='jedi',
            name='planet',
            field=models.ForeignKey(help_text='Планета на которой джедай обучает кандидатов', on_delete=django.db.models.deletion.CASCADE, to='hr_app.Planet', verbose_name='Планета'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_app.Planet', verbose_name='Планета обитания'),
        ),
        migrations.AddField(
            model_name='answer',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_app.Candidate', verbose_name='Кандидат'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_app.Question', verbose_name='Вопрос'),
        ),
    ]
