# Generated by Django 2.2.5 on 2020-07-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_registration", "0007_user_last_login"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]