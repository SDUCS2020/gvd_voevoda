# Generated by Django 5.1.1 on 2024-09-04 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClansModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('label', models.CharField(max_length=50, verbose_name='Значек')),
                ('alliance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voevoda_app.clansmodel', verbose_name='Альянс')),
            ],
            options={
                'verbose_name_plural': 'Кланы',
            },
        ),
        migrations.CreateModel(
            name='PlayersModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Ник')),
                ('level', models.IntegerField(default=1, verbose_name='Уровень')),
                ('umka_knight', models.IntegerField(default=1, verbose_name='Рыцарь')),
                ('umka_necro', models.IntegerField(default=1, verbose_name='Некромант')),
                ('umka_mag', models.IntegerField(default=1, verbose_name='Маг')),
                ('umka_elf', models.IntegerField(default=1, verbose_name='Эльф')),
                ('umka_barbar', models.IntegerField(default=1, verbose_name='Варвар')),
                ('umka_black_elf', models.IntegerField(default=1, verbose_name='Темный эльф')),
                ('umka_demon', models.IntegerField(default=1, verbose_name='Демон')),
                ('umka_dwarf', models.IntegerField(default=1, verbose_name='Гном')),
                ('umka_step_barb', models.IntegerField(default=1, verbose_name='Степной варвар')),
                ('umka_pharaon', models.IntegerField(default=1, verbose_name='Фараон')),
                ('gild_hunt', models.IntegerField(default=1, verbose_name='Гильдия Охотников')),
                ('gild_work', models.IntegerField(default=1, verbose_name='Гильдия Рабочих')),
                ('gild_card', models.IntegerField(default=1, verbose_name='Гильдия Картежников')),
                ('gild_thief', models.IntegerField(default=1, verbose_name='Гильдия Воров')),
                ('gild_ranger', models.IntegerField(default=1, verbose_name='Гильдия Рейнджеров')),
                ('gild_mers', models.IntegerField(default=1, verbose_name='Гильдия Наемников')),
                ('gild_tactic', models.IntegerField(default=1, verbose_name='Гильдия Тактиков')),
                ('gild_gard', models.IntegerField(default=1, verbose_name='Гильдия Стражей')),
                ('gild_seekers', models.IntegerField(default=1, verbose_name='Гильдия Искателей')),
                ('gild_leader', models.IntegerField(default=1, verbose_name='Гильдия Лидеров')),
                ('gild_blacksmith', models.IntegerField(default=1, verbose_name='Гильдия Кузнецов')),
                ('gild_gunsmith', models.IntegerField(default=1, verbose_name='Гильдия Оружейников')),
                ('clan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voevoda_app.clansmodel', verbose_name='Клан')),
            ],
            options={
                'verbose_name_plural': 'Игроки',
            },
        ),
    ]
