# Generated by Django 5.0.1 on 2024-01-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_flagged',
            field=models.BooleanField(default=False),
        ),
    ]