# Generated by Django 4.1.2 on 2022-10-14 10:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lawsuits', '0002_lawsuit'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawsuit',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('lawsuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawsuits.lawsuit')),
            ],
        ),
    ]