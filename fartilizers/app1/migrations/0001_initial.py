# Generated by Django 2.2.13 on 2020-10-09 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatagoryModel',
            fields=[
                ('catid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Typeofcatagory', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubcatagoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcatagory', models.CharField(max_length=50)),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.CatagoryModel')),
            ],
        ),
    ]
