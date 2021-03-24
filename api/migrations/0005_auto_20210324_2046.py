# Generated by Django 3.0 on 2021-03-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210324_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='addressOne',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='addressTwo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='city',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='email',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='industry',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='inventory',
            field=models.FileField(null=True, upload_to='user_directory_auth/'),
        ),
        migrations.AddField(
            model_name='business',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='business',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='business',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business',
            name='state',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='zipCode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
