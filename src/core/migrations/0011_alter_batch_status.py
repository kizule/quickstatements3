# Generated by Django 5.0.8 on 2024-09-23 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_batchcommand_data_type_verified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batch",
            name="status",
            field=models.IntegerField(
                choices=[
                    (-2, "Stopped"),
                    (-1, "Blocked"),
                    (0, "Initial"),
                    (1, "Running"),
                    (2, "Done"),
                ],
                db_index=True,
                default=0,
            ),
        ),
    ]
