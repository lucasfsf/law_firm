# Generated by Django 4.1.2 on 2022-10-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawsuits', '0004_alter_movement_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
