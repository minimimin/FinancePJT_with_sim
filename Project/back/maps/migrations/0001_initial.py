# Generated by Django 4.2.4 on 2023-11-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sido', models.TextField()),
                ('gungu', models.TextField()),
            ],
        ),
    ]
