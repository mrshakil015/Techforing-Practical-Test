# Generated by Django 5.1.4 on 2024-12-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='Due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
