# Generated by Django 5.0.7 on 2024-07-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_reward_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
