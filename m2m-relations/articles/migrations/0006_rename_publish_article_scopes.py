# Generated by Django 4.1.6 on 2023-02-03 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publish',
            new_name='scopes',
        ),
    ]
