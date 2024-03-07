# Generated by Django 5.0.2 on 2024-03-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_permissions",
        ),
        migrations.AlterField(
            model_name="patientprofile",
            name="sex",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
