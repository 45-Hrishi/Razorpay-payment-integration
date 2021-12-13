# Generated by Django 3.1.4 on 2021-12-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20211210_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='payment_id',
            new_name='order_id',
        ),
        migrations.AddField(
            model_name='donation',
            name='phone_no',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]