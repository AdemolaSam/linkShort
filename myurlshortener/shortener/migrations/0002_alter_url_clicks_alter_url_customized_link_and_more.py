# Generated by Django 4.2.11 on 2024-03-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shortener", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="url", name="clicks", field=models.IntegerField(blank=True)
        ),
        migrations.AlterField(
            model_name="url",
            name="customized_link",
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="url", name="expiry_date", field=models.DateTimeField(blank=True)
        ),
    ]
