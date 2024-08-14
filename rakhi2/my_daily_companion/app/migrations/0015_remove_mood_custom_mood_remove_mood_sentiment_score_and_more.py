# Generated by Django 5.0.7 on 2024-08-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_mood_intensity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mood',
            name='custom_mood',
        ),
        migrations.RemoveField(
            model_name='mood',
            name='sentiment_score',
        ),
        migrations.AlterField(
            model_name='mood',
            name='color',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='mood',
            name='intensity',
            field=models.FloatField(),
        ),
    ]
