# Generated by Django 3.2.11 on 2023-05-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0008_alter_submission_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='index',
            field=models.PositiveIntegerField(default=0),
        ),
    ]