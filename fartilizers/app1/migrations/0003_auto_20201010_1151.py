# Generated by Django 2.2.13 on 2020-10-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201010_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagorymodel',
            name='catid',
            field=models.IntegerField(default=False, primary_key=True, serialize=False),
        ),
    ]
