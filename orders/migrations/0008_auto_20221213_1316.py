# Generated by Django 2.2 on 2022-12-13 12:16

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.AlterField(
            model_name='order',
            name='book_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(django.utils.timezone.now)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(default='Ninguno', max_length=250),
        ),
    ]