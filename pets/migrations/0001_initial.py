# Generated by Django 3.0.8 on 2020-07-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('species', models.IntegerField()),
                ('age', models.CharField(max_length=10)),
            ],
        ),
    ]