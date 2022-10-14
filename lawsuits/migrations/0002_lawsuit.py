# Generated by Django 4.1.2 on 2022-10-14 10:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lawsuits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lawsuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('customer', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]