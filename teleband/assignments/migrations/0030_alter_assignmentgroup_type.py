# Generated by Django 3.2.11 on 2023-07-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0029_pieceplan_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentgroup',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]