# Generated by Django 5.1.1 on 2024-09-15 12:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voevoda_app', '0010_alter_fightsmodel_options_alter_fightsmodel_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighteventmodel',
            name='state',
            field=models.IntegerField(choices=[(1, 'Первоначальный сбор'), (2, 'Выбор бойцов'), (3, 'Идет бой'), (4, 'Завершен')], default=1),
        ),
        migrations.CreateModel(
            name='InviteModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('state', models.IntegerField(choices=[(1, 'Отправлено'), (2, 'Принято'), (3, 'Отказ')])),
                ('event_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voevoda_app.fighteventmodel', verbose_name='Ивент')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voevoda_app.personsmodel', verbose_name='Игрок')),
            ],
            options={
                'verbose_name_plural': 'Приглашение на ивент',
            },
        ),
    ]
