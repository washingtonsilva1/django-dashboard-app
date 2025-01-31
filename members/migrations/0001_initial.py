# Generated by Django 5.0.3 on 2024-04-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=155)),
                ('birth_date', models.DateField()),
                ('sex', models.BooleanField()),
                ('is_married', models.BooleanField()),
            ],
        ),
    ]
