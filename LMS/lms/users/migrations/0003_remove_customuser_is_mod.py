# Generated by Django 5.1.6 on 2025-02-23 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_mod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_mod',
        ),
    ]
