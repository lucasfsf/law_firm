# Generated by Django 4.1.2 on 2022-11-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_slug_alter_article_law_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
    ]