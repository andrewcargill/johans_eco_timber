# Generated by Django 3.2.16 on 2022-11-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_auto_20221104_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='submitted_date',
            field=models.DateTimeField(null=True),
        ),
    ]
