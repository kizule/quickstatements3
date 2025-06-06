# Generated by Django 5.0.9 on 2025-01-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_alter_batchcommand_operation"),
    ]

    operations = [
        migrations.AddField(
            model_name="batch",
            name="combine_commands",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="batchcommand",
            name="operation",
            field=models.TextField(
                blank=True,
                choices=[
                    ("create_item", "Create item"),
                    ("create_property", "Create property"),
                    ("set_statement", "Set statement"),
                    ("remove_statement_by_id", "Remove statement by id"),
                    ("remove_statement_by_value", "Remove statement by value"),
                    ("set_sitelink", "Set sitelink"),
                    ("set_label", "Set label"),
                    ("set_description", "Set description"),
                    ("remove_sitelink", "Remove sitelink"),
                    ("remove_label", "Remove label"),
                    ("remove_description", "Remove description"),
                    ("add_alias", "Add alias"),
                    ("remove_alias", "Remove alias"),
                ],
                null=True,
            ),
        ),
    ]
