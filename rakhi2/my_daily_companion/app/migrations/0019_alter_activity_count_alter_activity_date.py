# Generated by Django 5.0.7 on 2024-08-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
