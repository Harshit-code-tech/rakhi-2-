# Generated by Django 5.0.7 on 2024-08-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_mood_level_mood_intensity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='intensity',
            field=models.CharField(choices=[('VL', 'Very Low'), ('L', 'Low'), ('M', 'Moderate'), ('H', 'High'), ('VH', 'Very High')], max_length=2),
        ),
    ]