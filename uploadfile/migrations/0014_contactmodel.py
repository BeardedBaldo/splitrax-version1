# Generated by Django 3.0.8 on 2020-09-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0013_auto_20200825_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FromEmail', models.EmailField(max_length=254, null=True)),
                ('Subject', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
