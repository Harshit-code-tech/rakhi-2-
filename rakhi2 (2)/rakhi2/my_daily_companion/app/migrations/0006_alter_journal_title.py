# Generated by Django 5.0.7 on 2024-07-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_journal_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]