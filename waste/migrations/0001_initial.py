# Generated by Django 5.0.6 on 2024-05-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='nome')),
                ('score', models.SmallIntegerField(default=0, verbose_name='pontuação')),
            ],
        ),
    ]
