# Generated by Django 3.0 on 2021-03-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210324_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='inventory',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='phone',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
