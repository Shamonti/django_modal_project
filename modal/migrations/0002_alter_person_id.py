# Generated by Django 5.1.3 on 2024-11-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
