# Generated by Django 4.0.4 on 2022-05-02 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracker',
            options={'verbose_name': 'трекер', 'verbose_name_plural': 'трекеры'},
        ),
    ]
