# Generated by Django 3.2.12 on 2022-02-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    """Class defining the initial database schema for the CryptoTutor project."""

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['username', 'password'],
            },
        ),
    ]
