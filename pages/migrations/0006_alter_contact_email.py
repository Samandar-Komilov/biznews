# Generated by Django 5.0.4 on 2024-04-24 06:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator]),
        ),
    ]
