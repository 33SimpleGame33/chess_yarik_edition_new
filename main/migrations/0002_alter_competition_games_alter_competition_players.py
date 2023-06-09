# Generated by Django 4.2 on 2023-04-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='games',
            field=models.ManyToManyField(blank=True, to='main.game'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='players',
            field=models.ManyToManyField(blank=True, to='main.player'),
        ),
    ]
