# Generated by Django 4.2.9 on 2024-02-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='image',
            field=models.TextField(default='n/a', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bird',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
