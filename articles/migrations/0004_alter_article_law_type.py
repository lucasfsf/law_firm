# Generated by Django 4.1.2 on 2022-10-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_law_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='law_type',
            field=models.CharField(choices=[('CO', 'Constitucional'), ('TR', 'Tributário'), ('CI', 'Civil'), ('AD', 'Administrativo'), ('CR', 'Criminal'), ('CP', 'Empresarial'), ('FA', 'de Familia'), ('LA', 'Trabalhista'), ('OT', '(Outros)')], default='OT', max_length=2),
        ),
    ]
