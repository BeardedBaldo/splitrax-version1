# Generated by Django 3.0.8 on 2020-08-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0004_auto_20200806_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='OutputType',
            field=models.CharField(choices=[('mp3', 'mp3'), ('wav', 'wav')], max_length=5, null=True),
        ),
    ]
