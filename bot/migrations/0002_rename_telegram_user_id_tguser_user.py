# Generated by Django 4.2.1 on 2023-06-13 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tguser",
            old_name="telegram_user_id",
            new_name="user",
        ),
    ]
