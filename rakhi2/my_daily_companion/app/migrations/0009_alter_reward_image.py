# Generated by Django 5.0.7 on 2024-07-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_reward_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='image',
            field=models.ImageField(default='img/fallback.png', upload_to='rewards/'),
        ),
    ]