# Generated by Django 2.0.3 on 2018-03-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='closed_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
