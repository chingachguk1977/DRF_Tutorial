# Generated by Django 3.1.7 on 2021-02-21 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('address', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.sclass')),
            ],
        ),
    ]
