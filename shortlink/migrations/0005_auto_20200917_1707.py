# Generated by Django 2.2.4 on 2020-09-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0004_auto_20200916_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='short_path',
            field=models.CharField(blank=True, db_index=True, help_text='در صورتی که تعریف نشود\u200c، به صورت اتوماتیک ایجاد خواهد شد.', max_length=100, null=True, verbose_name='مسیر کوتاه شده'),
        ),
    ]
