# Generated by Django 2.0.6 on 2019-02-21 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='child_child_mom',
            new_name='child_mom',
        ),
        migrations.AlterField(
            model_name='mom',
            name='mom_phone_number',
            field=models.CharField(max_length=100),
        ),
    ]
