# Generated by Django 5.0.7 on 2024-08-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0015_remove_mood_custom_mood_remove_mood_sentiment_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='is_unlocked',
            field=models.BooleanField(default=False),
        ),
    ]
