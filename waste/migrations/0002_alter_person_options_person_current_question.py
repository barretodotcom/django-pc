# Generated by Django 5.0.6 on 2024-05-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Pessoa'},
        ),
        migrations.AddField(
            model_name='person',
            name='current_question',
            field=models.SmallIntegerField(default=1, verbose_name='questão atual'),
        ),
    ]
