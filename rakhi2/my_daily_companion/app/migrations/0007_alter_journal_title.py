# Generated by Django 5.0.7 on 2024-07-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_journal_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
