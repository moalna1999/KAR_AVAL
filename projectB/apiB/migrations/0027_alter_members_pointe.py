# Generated by Django 3.2 on 2021-05-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiB', '0026_alter_members_pointe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='pointe',
            field=models.IntegerField(choices=[('0', '0'), ('1', '1'), ('', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
    ]
