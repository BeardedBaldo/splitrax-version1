# Generated by Django 3.0.8 on 2020-08-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0003_auto_20200806_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(upload_to=''),
        ),
    ]
