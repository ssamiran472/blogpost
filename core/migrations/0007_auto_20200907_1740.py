# Generated by Django 3.0.9 on 2020-09-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200907_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content',
            field=models.TextField(default='content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.TextField(default='content'),
            preserve_default=False,
        ),
    ]
