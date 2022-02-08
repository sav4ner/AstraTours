# Generated by Django 3.0.3 on 2022-02-06 15:23

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('TourApp', '0006_auto_20220206_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='city',
            field=models.CharField(default=sqlalchemy.sql.expression.null, max_length=250),
        ),
        migrations.AddField(
            model_name='hotels',
            name='location',
            field=models.CharField(default=sqlalchemy.sql.expression.null, max_length=250),
        ),
    ]
