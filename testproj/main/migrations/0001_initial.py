# Generated by Django 3.2.10 on 2022-05-19 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=50)),
                ('value', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
        ),
    ]
