# Generated by Django 4.0.2 on 2022-05-07 17:29

from django.db import migrations


class Migration(migrations.Migration):
    """Django migration class to delete the Requests model."""

    dependencies = [
        ('cryptotutor', '0006_question_createddate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Requests',
        ),
    ]
