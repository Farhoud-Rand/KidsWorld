# Generated by Django 5.0.3 on 2024-05-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_rate_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='story',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
    ]