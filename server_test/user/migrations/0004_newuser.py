# Generated by Django 3.2.23 on 2024-01-18 01:02

from django.db import migrations, models
import utils.validator.validator


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_delete_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30, unique=True, validators=[utils.validator.validator.validate_phone_number])),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, unique=True, validators=[utils.validator.validator.validate_email])),
            ],
        ),
    ]
