# Generated by Django 3.2.16 on 2022-11-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_alter_quote_submitted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deadline',
            field=models.DateField(),
        ),
    ]
