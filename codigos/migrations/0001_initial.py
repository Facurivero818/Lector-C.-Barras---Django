# Generated by Django 4.2.1 on 2023-07-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=70)),
                ('producto', models.CharField(max_length=70)),
            ],
        ),
    ]
