# Generated by Django 3.0.8 on 2020-08-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0008_auto_20200807_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='audio',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
