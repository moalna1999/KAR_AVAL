# Generated by Django 3.2 on 2021-05-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiB', '0020_adminstor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminstors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6000)),
                ('ADM_ID', models.ManyToManyField(to='apiB.Members')),
            ],
        ),
        migrations.DeleteModel(
            name='Adminstor',
        ),
    ]
