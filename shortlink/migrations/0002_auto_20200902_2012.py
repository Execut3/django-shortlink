# Generated by Django 2.2.5 on 2020-09-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortlink',
            options={'verbose_name': 'Shortlink'},
        ),
        migrations.RemoveField(
            model_name='shortlink',
            name='long_url',
        ),
        migrations.RemoveField(
            model_name='shortlink',
            name='short_url',
        ),
        migrations.AddField(
            model_name='shortlink',
            name='full_url',
            field=models.CharField(default='', max_length=500, verbose_name='Real URL to be shorten'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shortlink',
            name='short_path',
            field=models.CharField(db_index=True, default='', max_length=100, verbose_name='Shorten Path ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Presentation name for url'),
        ),
        migrations.AlterModelTable(
            name='shortlink',
            table='shortlink',
        ),
    ]