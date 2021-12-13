# Generated by Django 3.1.4 on 2021-12-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='donation',
            new_name='Amount',
        ),
        migrations.AddField(
            model_name='donation',
            name='email',
            field=models.EmailField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
