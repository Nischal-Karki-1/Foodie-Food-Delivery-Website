# Generated by Django 4.0.6 on 2022-10-15 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='item_name',
            new_name='name',
        ),
    ]
