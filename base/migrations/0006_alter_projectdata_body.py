# Generated by Django 4.0.1 on 2022-03-17 13:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_project_projectdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdata',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
