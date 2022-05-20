# Generated by Django 4.0.4 on 2022-05-03 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0002_alter_tracker_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracker',
            options={'ordering': ['name'], 'verbose_name': 'трекер', 'verbose_name_plural': 'трекеры'},
        ),
        migrations.AddField(
            model_name='tracker',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='trackers/photos', verbose_name='фотография'),
        ),
    ]