# Generated by Django 5.0.1 on 2024-03-07 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('empname', models.CharField(max_length=20)),
                ('empsalary', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
