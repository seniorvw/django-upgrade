# Generated by Django 2.2.5 on 2021-08-05 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0016_auto_20210805_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
