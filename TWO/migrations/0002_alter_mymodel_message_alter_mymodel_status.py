# Generated by Django 5.0.1 on 2024-05-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='message',
            field=models.TextField(default='default message'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='status',
            field=models.CharField(default='default status', max_length=100),
        ),
    ]
