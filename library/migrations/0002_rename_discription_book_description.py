# Generated by Django 4.1.1 on 2022-10-02 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='discription',
            new_name='description',
        ),
    ]
