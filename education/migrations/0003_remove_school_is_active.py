# Generated by Django 3.1.7 on 2021-04-01 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_school_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='is_active',
        ),
    ]
