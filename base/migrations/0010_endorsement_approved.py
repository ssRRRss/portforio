# Generated by Django 4.0.1 on 2022-03-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
