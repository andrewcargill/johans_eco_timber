# Generated by Django 3.2.16 on 2022-11-04 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_alter_quote_submitted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='submitted_date',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
