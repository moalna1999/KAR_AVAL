# Generated by Django 3.2 on 2021-05-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiB', '0022_alter_members_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='activity',
            field=models.BooleanField(choices=[('Disabled', False), (True, 'Active')], max_length=600),
        ),
    ]
