# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 17:08
from __future__ import unicode_literals

from django.db import migrations

PLANETS = (
    'Alderaan',
    'Cato Neimoidia',
    'Coruscant',
    'Chandrila',
    'Dagobah',
    'Endor',
    'Hoth',
    'Jakku',
    'Naboo',
    'Tatooine',
    'Shili',
)

JEDI = (
    ('Yoda', 'Dagobah'),
    ('Mace Windu', 'Coruscant'),
    ('Qui-Gon Jinn', 'Naboo'),
    ('Obi-Wan Kenobi', 'Tatooine'),
    ('Princess Leia Organa', 'Alderaan')
)

QUESTIONS = (
    'В качестве основного оружия джедаи использовали...',
    'Как назывался корабль Хана Соло?',
    'Мастеру Йоде лет было сколько?'
)

CANDIDATES = (
    (
        'Anakin Skywalker', 'Tatooine', 12, 'anakin@collkid.com', 
        ('Звуковые мячи', 'Столетний сокол', '700')),
    (
        'Ben Solo', 'Chandrila', 6, 'ben@ikillmyfather.com',
        ('Силу', 'Сова тысячелетия', '900')),
    (
        'Ahsoka Tano', 'Shili', 12, 'ahsoka@anakinonelove.com',
        ('Световые лучи', 'Орел миллионник', '150')),
)


def create_planets(apps, schema_editor):
    Planet = apps.get_model('hr_app', 'Planet')
    for planet in PLANETS:
        Planet.objects.create(name=planet)


def create_jedi(apps, schema_editor):
    Jedi = apps.get_model('hr_app', 'Jedi')
    Planet = apps.get_model('hr_app', 'Planet')
    for jedi in JEDI:
        jedi_name, jedi_planet = jedi
        planet = Planet.objects.get(name=jedi_planet)
        Jedi.objects.create(name=jedi_name, planet=planet)


def create_exam(apps, schema_editor):
    Exam = apps.get_model('hr_app', 'Exam')
    Question = apps.get_model('hr_app', 'Question')
    exam = Exam.objects.create(code='c8sdfsd3')
    for question in QUESTIONS:
        Question.objects.create(exam=exam, text=question)


def create_candidates(apps, schema_editor):
    Candidate = apps.get_model('hr_app', 'Candidate')
    Planet = apps.get_model('hr_app', 'Planet')
    Question = apps.get_model('hr_app', 'Question')
    Answer = apps.get_model('hr_app', 'Answer')
    for candidate in CANDIDATES:
        name, planet, age, email, answers = candidate
        planet = Planet.objects.get(name=planet)
        candidate = Candidate.objects.create(
            name=name, planet=planet, age=age, email=email)
        for index, question in enumerate(QUESTIONS):
            q = Question.objects.get(text=question)
            Answer.objects.create(
                candidate=candidate, question=q, answer=answers[index])


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_planets, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(
            create_jedi, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(
            create_exam, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(
            create_candidates, reverse_code=migrations.RunPython.noop),
    ]
