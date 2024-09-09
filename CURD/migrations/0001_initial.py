# Generated by Django 5.0.4 on 2024-09-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('sal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dno', models.IntegerField()),
            ],
        ),
    ]